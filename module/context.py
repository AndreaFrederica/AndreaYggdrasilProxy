import module
from module import configIO
from module import tools
from module import playerCache



config:configIO.config

YggdrasilServers:list[tools.YggdrasilServer]
player_cache:playerCache.PlayerCache
#TODO 完成PlayerCache
server_pid2server:dict()
