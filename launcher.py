import sys
from module import context, loadConfig, log, playerCache
loadConfig.init()
log.init()
playerCache.init()
#TODO 完成PlayerCache
log.info("[Config] Config Loaded")
from main import app
if __name__ == "__main__":
    if(context.config["Enable"]):
        import uvicorn
        server_url = (f"http://{context.config['IP']}:{context.config['Port']}")
        log.info(f"Server running on {server_url}")
        try:
            uvicorn.run(
                app,
                host=context.config["IP"],
                port=context.config["Port"]
            )
        except KeyboardInterrupt:
            log.warning("\nApplication exit!")
        except Exception:
            log.error(*sys.exc_info())
    else:
        raise ValueError("CONFIG NOT ENABLE")