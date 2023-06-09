import time
from datetime import datetime as dt
host_temp='host'
host = 'C:\Windows\System32\drivers\etc'
redirect = '127.0.0.1'
weblist = ['www.facebook.com','facebook.com']
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('work')
    else:
        print('relax')
    time.sleep(6)