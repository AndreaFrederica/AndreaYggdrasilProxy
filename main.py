import requests

from fastapi import FastAPI, Query, Response
from module import loadConfig
from module import log, context



app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sessionserver/session/minecraft/hasJoined")
def has_joined(
    # 从查询参数中获取 username 和 serverId 的值，使用 Query 类来设置一些校验规则
    username: str = Query(..., min_length=3, max_length=16, regex="^[a-zA-Z0-9_]+$"),
    serverId: str = Query(..., min_length=1, max_length=64)
):
    log.info(f"Player {username} try to join Server {serverId}")
    #? 遍历验证服务器列表
    for server in context.YggdrasilServers:
        url = (f"{server.url}/session/minecraft/hasJoined?username={username}&serverId={serverId}")
        log.info(url)
        response = requests.get(url)
        # 判断响应的状态码是否为 200，表示成功
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
            return neo_response
        else:
            log.warning(f"Can't find player on server {server.name}")
    
    # 返回一个204错误，表示没有找到玩家的信息
    log.error(f"Error 204 找不到玩家信息")
    return Response(status_code=204)
