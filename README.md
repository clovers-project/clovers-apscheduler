# clovers_apscheduler

_✨ clovers APScheduler 定时任务插件 ✨_

<div align="center">
<img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="python">
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/KarisAya/clovers_apscheduler.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/clovers_apscheduler">
  <img src="https://img.shields.io/pypi/v/clovers_apscheduler.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/clovers_apscheduler">
  <img src="https://img.shields.io/pypi/dm/clovers_apscheduler" alt="pypi download">
</a>
</div>

## 使用方式

```python
from clovers_apscheduler import scheduler
@scheduler.scheduled_job("cron", hour="*/4", misfire_grace_time=120)
async def _():
    pass
```

## 配置项

`apscheduler` 的相关配置

参考 [配置 scheduler](https://apscheduler.readthedocs.io/en/latest/userguide.html#scheduler-config)，[配置参数](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler)

配置需要包含 `prefix: apscheduler.`

默认配置：

```json
{ "apscheduler.timezone": "Asia/Shanghai" }
```
