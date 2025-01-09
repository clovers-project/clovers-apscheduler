from apscheduler.schedulers.asyncio import AsyncIOScheduler
from clovers import Plugin
from clovers.logger import logger
from clovers.config import config as clovers_config

scheduler_config: dict = {"apscheduler.timezone": "Asia/Shanghai"}

config_key = __package__
config_data = clovers_config.get(config_key, scheduler_config)
clovers_config[config_key] = config_data
scheduler_config.update(config_data)


plugin = Plugin()
scheduler = AsyncIOScheduler()
scheduler.configure(**scheduler_config)


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
