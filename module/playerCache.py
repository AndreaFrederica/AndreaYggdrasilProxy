from typing import Any
import time
import threading

from module import context
from module import log
from module.log import info

class PlayerCache:
    gc_time: int = 172800
    #? 48h为GC阈值
    def __init__(self) -> None:
        #? 使用 object.__setattr__ 来避免无限递归
        object.__setattr__(self, 'player_data', dict())
        object.__setattr__(self, 'key_timestamp', dict())
        #? 记录下每个KV的时间戳 以便回收
    def set(self, __key: str, __value: Any ) -> None:
        self.player_data[__key] = __value
        self.key_timestamp[__key] = int(time.time())
    def get(self, __key: str) -> None:
        self.key_timestamp[__key] = int(time.time())
        return self.player_data[__key]
    def __setattr__(self, __key: str, __value: Any) -> None:
        #? 调用父类的 __setattr__ 方法，以保证属性功能不被破坏
        super().__setattr__(__key, __value)
        #? 保存秒级精度时间戳
        pass
    def __getattr__(self, __key: str) -> Any:
        #? 处理属性不存在的情况，抛出一个 AttributeError 异常
        if __key not in self.player_data:
            raise AttributeError(__key)
        return self.get(__key)
    def getTimestamp(self, __key) -> int:
        return self.key_timestamp(__key)
    def gc(self) -> None:
        timestamp = int(time.time())
        #? 使用 list(self.key_timestamp.keys()) 来避免 RuntimeError 异常
        for key in list(self.key_timestamp.keys()):
            if(timestamp - self.key_timestamp[key] >= self.gc_time):
                del self.key_timestamp[key]
                del self.player_data[key]
    def gcTask(self) -> None:
        while(True):
            self.gc()
            #log.debug(f"完成PlayerDataCacheGC PlayerCache : {self.player_data}")
            time.sleep(60)

def init():
    #? 创建一个 PlayerCache 的实例，并传递 self 参数
    context.player_cache:PlayerCache = PlayerCache()
    gc_thread = threading.Thread(target=context.player_cache.gcTask, name='player_data_gc_task')
    gc_thread.setDaemon(True)
    #? 设置为守护进程 使其能随着主进程退出而退出
    gc_thread.start()
    log.info("[PlayerDataCache] PlayerData GC-Thread Starting")
    log.info("[PlayerDataCache] PlayerDataCache Loaded")
#TODO 完成PlayerCache
