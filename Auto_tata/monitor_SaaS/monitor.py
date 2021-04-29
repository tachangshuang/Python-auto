import sys
import threading
import time

from monitor_SaaS.operation import monitor_interface

sys.path.append(r'/Auto_tata/monitor_SaaS/')

def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


def time_check():
    second = sleeptime(0, 0, 5)
    while 1 == 1:
        time.sleep(second)
        monitor_interface()


# 创建定时任务监控

timer = threading.Timer(6, time_check())
timer.start()


