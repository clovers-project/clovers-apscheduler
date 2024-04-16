from pydantic import BaseModel


class Config(BaseModel):
    scheduler_config: dict = {"apscheduler.timezone": "Asia/Shanghai"}
