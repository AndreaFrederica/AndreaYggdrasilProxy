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
        pass