from datetime import datetime as dt

def time_delta(t1, t2):
    # define time format
    timeformat = '%a %d %b %Y %H:%M:%S %z'
    absolute_diff = abs(dt.strptime(t1, timeformat) - dt.strptime(t2, timeformat)).total_seconds()

    return int(absolute_diff)


x = 'Sat 02 May 2015 19:54:36 +0530'
y = 'Fri 01 May 2015 13:54:36 -0000'

print(time_delta(x, y))