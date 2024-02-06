import json
import signal
from pydantic import BaseModel
import requests

from fastapi import Body, FastAPI, Query, Response
from typing import Any, List
from module import loadConfig, neoRequests
from module import log, context
from module import playerCache
from module.playerCache import PlayerCache
from module.tools import YggdrasilServer
from module.errorCollectionTools import tryFunction


app = FastAPI()



@app.get("/")
@tryFunction
def read_root():
    return {"Hello": "World"}

@app.post("/api/profiles/minecraft")
@tryFunction
def profiles_minecraft(req_body:List[str]):
    log.info(f"Server try to get PlayerInfo req = {str(req_body)}")
    players:list = list(req_body)
    server2player_group:dict = dict()
    try_offical_list:list = list()
    #? 服务器pid对应的玩家组
    for player in players:
        try:
            server_pid:int = context.player_cache.get(player)
        except:
            log.warning(f"服务器所查询玩家尚未在玩家缓存中找到 将尝试根据默认顺序查询")
            try_offical_list.append(player)
            continue
        if(isinstance (server2player_group[server_pid],list)):
            server2player_group[server_pid] += [player]
        else:
            server2player_group[server_pid] = [player]
    responses:list = list()
    for server_pid in server2player_group.keys():
        server:YggdrasilServer = context.server_pid2server[server_pid]
        url = server.profile_api
        data=json.dumps(server2player_group[server_pid])
        log.info(f"Url = {url} Data = {data}")
        response = neoRequests.post(url,data=data,proxies=server.proxies,timeout=server.timeout,port=server.port)
        #? 向上游服务器发送请求 请求玩家数据
        if response.status_code == 200:
            log.success(f"Get PlayerData from {server.name}")
            responses.append(response)
        else:
            log.error(f"Can't get PlayerData from {server.name}")
    #? 完成玩家缓存内数据查询 下面为未在缓存内的玩家的默认顺序查询
    for server in context.YggdrasilServers:
        url = server.profile_api
        log.debug(try_offical_list)
        data = json.dumps(try_offical_list)
        log.info(f"Url = {url} Data = {data}")
        response = neoRequests.post(url,data=data,proxies=server.proxies,timeout=server.timeout,port=server.port)
        #? 向上游服务器发送请求 请求玩家数据
        if response.status_code == 200:
            log.success(f"Get PlayerData from {server.name}")
            responses.append(response)
            break
        else:
            log.error(f"Can't get PlayerData from {server.name}")
    #? 至此完成所有上游服务器的请求 下面为合并请求数据
    neo_response_data:list = list()
    player_ls:list = list()
    for __requests in responses:
        player_ls.append(__requests.json())
        for __player in player_ls:
            neo_response_data.append(__player)
    log.info(f"All PlayerData = {str(neo_response_data)}")
    return neo_response_data

@app.get("/sessionserver/session/minecraft/hasJoined")
@tryFunction
def has_joined(
    # 从查询参数中获取 username 和 serverId 的值，使用 Query 类来设置一些校验规则
    username: str = Query(..., min_length=3, max_length=16, pattern=r"^([a-zA-Z0-9_]+)$"),
    serverId: str = Query(..., min_length=1, max_length=64)
):
    log.info(f"Player {username} try to join Server {serverId}")
    #? 遍历验证服务器列表
    for server in context.YggdrasilServers:
        url = (f"{server.url}/session/minecraft/hasJoined?username={username}&serverId={serverId}")
        log.info(url)
        response = neoRequests.get(url,proxies=server.proxies,timeout=server.timeout,port=server.port)
        #! 好几次修正堆得屎山 别学
        #? 判断响应的状态码是否为 200，表示成功
        if response.status_code == 200:
            log.success(f"Find player on server {server.name}")
            #! 在返回值中标记验证服务器名字
            neo_response = response.json()
            neo_response["properties"].append(
                {
                    "name" : "AndreaYggdrasilProxy_YggdrasilServerName",
                    "value" : f"{server.name}",
                    "signature" : "="
                }
            )
            # 返回响应的 JSON 数据，作为 API 的返回值
            log.info(neo_response)
            context.player_cache.set(username,server.pid)
            #? 保存玩家和使用的验证服务器到缓存
            #TODO 完成PlayerCache
            return neo_response
        else:
            log.warning(f"Can't find player on server {server.name}")
    
    # 返回一个204错误，表示没有找到玩家的信息
    log.error(f"Error 204 找不到玩家信息")
    return Response(status_code=204)
