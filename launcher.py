from module import context, loadConfig, log
loadConfig.init()
log.init()
log.info("[Config] Config Loaded")
from main import app
if __name__ == "__main__":
    if(context.config["Enable"]):
        import uvicorn
        server_url = (f"http://{context.config['IP']}:{context.config['Port']}")
        log.info(f"Server running on {server_url}")
        uvicorn.run(
            app, host=context.config["IP"],
            port=context.config["Port"]
            )
    else:
        raise ValueError("CONFIG NOT ENABLE")