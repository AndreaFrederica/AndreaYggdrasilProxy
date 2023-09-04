import sys
import os
from loguru import logger


"""
loguru提供了七层日志层级，或者说七种日志类型。
生产环境中，常常在不同场景下使用不用的日志类型，用于处理各种问题。
每种类型的日志有一个整数值，表示日志层级，我们成为log level no。

TRACE (5): 用于记录程序执行路径的细节信息，以进行诊断。
DEBUG (10): 开发人员使用该工具记录调试信息。
INFO (20): 用于记录描述程序正常操作的信息消息。
SUCCESS (25): 类似于INFO，用于指示操作成功的情况。
WARNING (30): 警告类型，用于指示可能需要进一步调查的不寻常事件。
ERROR (40): 错误类型，用于记录影响特定操作的错误条件。
CRITICAL (50): 严重类型，用于记录阻止核心功能正常工作的错误条件。
"""
log_filename = "loguru.log"
log_path = "log"
if(not os.path.exists):
    os.mkdir(log_path)
log_fullpath= f"{log_path}/{log_filename}"

logger.remove(0)
logger.add(log_fullpath)
#logger.add(sys.stderr, format="{time} | {level} | {message}")
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level> | {level} | {message}</level>")

logger.debug("Happy logging with Loguru!")


trace = logger.trace
debug = logger.debug
info = logger.info
success = logger.success
warning = logger.warning
error = logger.error
critical = logger.critical


""" def trace(message: str, *args, **kwargs):
    logger.trace(message, *args, **kwargs)

def debug(message: str, *args, **kwargs):
    logger.debug(message, *args, **kwargs)

def info(message: str, *args, **kwargs):
    logger.info(message, *args, **kwargs)

def success(message: str, *args, **kwargs):
    logger.success(message, *args, **kwargs)

def warning(message: str, *args, **kwargs):
    logger.warning(message, *args, **kwargs)

def error(message: str, *args, **kwargs):
    logger.error(message, *args, **kwargs)

def critical(message: str, *args, **kwargs):
    logger.critical(message, *args, **kwargs) """
