def pyBool2JsonStr(value: bool) -> str:
    if(value):
        return "true"
    else:
        return "false"

class YggdrasilServer:
    def __init__(self,level: int, name: str, url: str) -> None:
        self.level = level
        self.name = name
        self.url = url
        self.proxies = None
        self.timeout = 5
        #? 默认五秒超时
        self.port = None
        #? None即为不指定端口
        self.profile_api = None
        pass
    def serverTypeCheck(self):
        if("/api/yggdrasil/sessionserver" in self.url):
            return "unofficial"
        elif("sessionserver.mojang.com" in self.url):
            return "official"
        else:
            return "unknown"
            pass
    def setUnofficialProfileAPI(self):
        self.profile_api = self.url.replace("/api/yggdrasil/sessionserver", "/api/profiles/minecraft")
    def setOfficialProfileAPI(self):
        self.profile_api = self.url
        #! ProfileAPI资料不完全 尚未完成 禁止使用