import requests

from fastapi import FastAPI, Query, Response
from typing import Any
from module import loadConfig
from module import log, context
from module import playerCache
from module.playerCache import PlayerCache



app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/profiles/minecraft")
def profiles_minecraft(req_body: Any):
    print(req_body)

@app.get("/sessionserver/session/minecraft/hasJoined")
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
        if(server.proxies != None):
            if(server.port != None):
                response = requests.get(url,proxies=server.proxies,timeout=server.timeout,port=server.port)
            else:
                response = requests.get(url,proxies=server.proxies,timeout=server.timeout)
        else:
            if(server.proxies != None):
                response = requests.get(url,timeout=server.timeout,port=server.port)
            else:
                response = requests.get(url,timeout=server.timeout)
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
            #context.player_cache.set(username,server.url)
            #? 保存玩家和使用的验证服务器到缓存
            #TODO 完成PlayerCache
            return neo_response
        else:
            log.warning(f"Can't find player on server {server.name}")
    
    # 返回一个204错误，表示没有找到玩家的信息
    log.error(f"Error 204 找不到玩家信息")
    return Response(status_code=204)
