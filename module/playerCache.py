from typing import Any
import time
import threading

class PlayerCache:
    gc_time: int = 172800
    #? 48h为GC阈值
    def __init__(self) -> None:
        self.player_data = dict()
        self.key_timestamp = dict()
        #? 记录下每个KV的时间戳 以便回收
    def set(self, __key: str, __value: Any ) -> None:
        self[__key] = __value
    def get(self, __key: str) -> None:
        return self[__key]
    def __setattr__(self, __key: str, __value: Any) -> None:
        self.player_data[__key] = __value
        self.key_timestamp[__key] = int(time.time())
        #? 保存秒级精度时间戳
        pass
    def __getattr__(self, __key: str) -> Any:
        self.key_timestamp[__key] = int(time.time())
        return self.player_data[__key]
    def getTimestamp(self, __key) -> int:
        return self.key_timestamp(__key)
    def gc(self) -> None:
        timestamp = int(time.time())
        for key in self.key_timestamp.keys():
            if(timestamp - self.key_timestamp[key] >= self.gc_time):
                del self.key_timestamp[key]
                del self.player_data[key]
    def gcTask(self) -> None:
        while(True):
            self.gc()
            time.sleep(60)

def init():
    gc_thread = threading.Thread(target=PlayerCache.gcTask, name='player_data_gc_task')
    gc_thread.start()
    
    
#TODO 完成PlayerCache