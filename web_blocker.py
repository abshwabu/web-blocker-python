import time
from datetime import datetime as dt
host_temp='hosts'
host = 'C:\Windows\System32\drivers\etc'
redirect = '127.0.0.1'
weblist = ['www.facebook.com','facebook.com']
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,23):
        print('work')
        with open(host_temp,'r+') as file:
            content = file.read()
            print(content)
    else:
        print('relax')
    time.sleep(6)