import threading
from tata.operation import time_check

# 创建定时任务监控

timer = threading.Timer(6, time_check())
timer.start()
