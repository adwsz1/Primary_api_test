# -*- coding:utf-8 -*-
# author:WangGang
# datetime:2020/5/27 2:02 下午
# software: PyCharm
from apscheduler.schedulers.blocking import BlockingScheduler
import os

'''
cron:
year (int|str) – 4-digit year
month (int|str) – month (1-12)
day (int|str) – day of the (1-31)
week (int|str) – ISO week (1-53)
day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
hour (int|str) – hour (0-23)
minute (int|str) – minute (0-59)
second (int|str) – second (0-59)
start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
'''

'''
date:
run_date (datetime|str) – the date/time to run the job at
timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already
'''

'''
interval:
weeks (int) – number of weeks to wait
days (int) – number of days to wait
hours (int) – number of hours to wait
minutes (int) – number of minutes to wait
seconds (int) – number of seconds to wait
start_date (datetime|str) – starting point for the interval calculation
end_date (datetime|str) – latest possible date/time to trigger on
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations
'''
import time


def job1():
    print("kill -9 $(ps -ef | grep 3000 | grep allure | awk '{print $2}')")
    os.popen("kill -9 $(ps -ef | grep 3000 | grep allure | awk '{print $2}')").read()
    print("/bin/bash run.sh")
    os.popen("/bin/bash run.sh").read()


def job2():
    print("kill -9 $(ps -ef | grep 3000 | grep allure | awk '{print $2}')")
    os.popen("kill -9 $(ps -ef | grep 3000 | grep allure | awk '{print $2}')").read()
    print("/bin/bash run.sh")
    os.popen("/bin/bash run.sh").read()


scheduler = BlockingScheduler()
scheduler.add_job(job1, 'interval', minutes=5, args=[])
scheduler.add_job(job2, 'interval', minutes=10, args=[])
"""'interval', hours=2, start_date='2018-01-10 09:30:00''"""
# scheduler.add_job(job, 'interval', weeks='mon', start_date='2018-01-10 09:30:00', args=[])

scheduler.start()
