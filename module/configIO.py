import json
import module
import os
import config
import pyjson5

#! Module Config
path = "config"
# * End Config



if (not os.path.exists(path)):
    os.mkdir(path)


class Config():
    global path

    def __init__(self, name: str) -> None:
        global path
        self.config: dict = dict()
        self.config_path = f"{path}/{name}.json5"
        if (os.path.exists(self.config_path)):
            self.read()
        pass

    def __getConfigFileObj(self, mode: str) -> object:
        self.file_obj = open(self.config_path, mode=mode,
                             encoding=config.encode)
        return self.file_obj

    def setRAW_STR(self, RAW_STR) -> None:
        self.__getConfigFileObj("w+")
        self.file_obj.write(RAW_STR)
        self.file_obj.close()

    def defaultCheck(self, *names: str) -> bool:
        for i in names:
            if (self.get(i) == None):
                return False
        return True

    def read(self) -> None:
        self.__getConfigFileObj("r")
        try:
            self.config = pyjson5.decode_io(self.file_obj)
        except:
            pass
        self.file_obj.close()

    def commit(self) -> None:
        self.__getConfigFileObj("w+")
        self.file_obj.write(json.dumps(
            self.config, sort_keys=True, indent=4, separators=(',', ':')))
        self.file_obj.close()

    def setDefault(self, name: str, obj: object) -> object:
        key = name
        if (self.get(key) == None):
            self.set(key, obj)
        return self.get(key)

    def set(self, key: str, val: object) -> None:
        self.config[key] = val

    def get(self, key: str) -> object:
        if (key in self.config.keys()):
            return self.config[key]
        else:
            return None
    #! 运算符重载部分

    def __getitem__(self, key: str) -> object:
        return self.get(key)

    def __setitem__(self, key: str, val: object) -> None:
        self.set(key, val)

    def __len__(self) -> int:
        return len(self.config)

#* Tools function
def pyBool2Json(flag:bool) -> str:
    if(flag):
        return "true"
    else:
        return "false"
p2J = pyBool2Json