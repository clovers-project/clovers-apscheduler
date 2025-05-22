from apscheduler.schedulers.asyncio import AsyncIOScheduler
from clovers import Plugin
from clovers.logger import logger
from clovers.config import Config as CloversConfig

config_data = CloversConfig.environ().setdefault("apscheduler", {})
assert isinstance(config_data, dict)
default_config = {"apscheduler.timezone": "Asia/Shanghai"}
config_data.update({k: v for k, v in default_config.items() if k not in config_data})

plugin = Plugin()
scheduler = AsyncIOScheduler(config_data)


@plugin.startup
async def _():
    if not scheduler.running:
        logger.debug("Starting scheduler")
        scheduler.start()
    else:
        logger.debug("Scheduler already running")


@plugin.shutdown
async def _():
    if scheduler.running:
        logger.debug("Shutting down scheduler")
        scheduler.shutdown()
    else:
        logger.debug("Scheduler not running")


__plugin__ = plugin
