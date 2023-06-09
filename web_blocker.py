import time
from datetime import datetime as dt
host_temp='hosts'
host = 'C:\Windows\System32\drivers\etc'
redirect = '127.0.0.1'
weblist = ['www.facebook.com','facebook.com']
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,17):
        print('work')
        with open(host,'r+') as file:
            content = file.read()
            for website in weblist:
                if website in content:
                    pass
                else:
                    file.write('\n'+redirect+' '+website)
    else:
        print('relax')
        with open(host,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in weblist):
                    file.write(line)
            file.truncate()
    time.sleep(6)