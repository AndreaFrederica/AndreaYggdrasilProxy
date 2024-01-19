# * 自定义默认配置文件字符串
from module import configIO, context, log, tools

#! 默认配置
enable = False
log = False

cstr = (
    f"""{{
    //* AndreaYggdrasilProxy
    Enable : {tools.pyBool2JsonStr(enable)},
    Log: {tools.pyBool2JsonStr(log)},
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
    context.server_pid2server = dict()
    context.config: configIO.Config = configIO.Config(
        "AndreaYggdrasilProxy")
    if(not context.config.defaultCheck("YggdrasilServers","Enable","IP","Port","Log")):
        context.config.setRAW_STR(cstr)
    context.config.read()
    enable = context.config["enable"]

    context.YggdrasilServers = list()
    pid = 0
    for server_info in context.config["YggdrasilServers"]:
        server = tools.YggdrasilServer(
            level = server_info["Level"],
            name = server_info["Name"],
            url = server_info["Url"],
            pid = pid
            )
        pid += 1
        #? pid 为自增id 用于鉴别服务器实例
        if("Proxies" in server_info):
            server.proxies = server_info["Proxies"]
            #! 若存在代理服务器则为此服务器注册使用代理服务器 请参照request库所支持格式填写
            #? Proxies : {
            #?    'http': 'http://127.0.0.1:20808',
            #?    'https': 'http://127.0.0.1:20808'
            #?}
        if("Timeout" in server_info):
            server.timeout = server_info["Timeout"]
            #? 若指定超时时间则自定义超时时间 默认为5秒
        if("Port" in server_info):
            server.port = server_info["Port"]
            #? 若指定超时时间则自定义超时时间 默认为5秒
        if("ProfileAPI" in server_info):
            server.profile_api = server_info["ProfileAPI"]
            #? 若指定ProfileAPI则指定ProfileAPI 否则进行API推算
        else:
            server.autoProfileAPI()
        context.YggdrasilServers.append(server)
        context.server_pid2server[server.pid] = server
        #? 注册pid到server的映射
    # 使用 sorted() 函数来对列表进行排序，指定 key 参数为 lambda 表达式，表示按照实例的 level 属性来排序
    context.YggdrasilServers = sorted(context.YggdrasilServers, key=lambda server: server.level)




