# * 自定义默认配置文件字符串
from module import configIO, context, log, tools

#! 默认配置
enable = False

cstr = (
    f"""{{
    //* AndreaYggdrasilProxy
    Enable : true,
    IP : "0.0.0.0",
    Port : 32217,
    YggdrasilServers : [
        {{
            //! Mojang 官方验证服务器
            Level : 0,
            Name: "Mojang",
            //! 服务器等级 越小优先级越高
            Url : "https://sessionserver.mojang.com"
        }},
        {{
            //! LittleSkin
            Level : 1,
            Name: "LittleSkin",
            Url : "https://littleskin.cn/api/yggdrasil/sessionserver"
        }},
    ]
}}
"""
)
# ? End


def init():
    global server_url_list, enable
    context.config: configIO.Config = configIO.Config(
        "AndreaYggdrasilProxy")
    if(not context.config.defaultCheck("YggdrasilServers","Enable","IP","Port")):
        context.config.setRAW_STR(cstr)
    context.config.read()
    enable = context.config["enable"]
    log.info("[Config] Config Loaded")

def loadServers():
    context.YggdrasilServers = list()
    for server_info in context.config["YggdrasilServers"]:
        server = tools.YggdrasilServer(
            level = server_info["Level"],
            name = server_info["Name"],
            url = server_info["Url"]
            )
        context.YggdrasilServers.append(server)
    # 使用 sorted() 函数来对列表进行排序，指定 key 参数为 lambda 表达式，表示按照实例的 level 属性来排序
    context.YggdrasilServers = sorted(context.YggdrasilServers, key=lambda server: server.level)

init()
loadServers()


