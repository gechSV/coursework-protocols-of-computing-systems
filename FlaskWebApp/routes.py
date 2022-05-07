import datetime
from datetime import *


def saveLog(log):
    dt_now = datetime.now()
    f = open('ServerLogs.txt', 'a')
    f.write('\n' + dt_now.strftime('%Y-%m-%d %H:%M:%S') + '\n   ' + log + '\n')
    f.close()
