#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    times = get_time_dict(t1, t2)

    print(times)






def get_time_dict(t1, t2):
    times = {}

    for i, t in enumerate([t1, t2]):

        tdata = re.match('(\w{3})\s(\d{2})\s(\w+)\s(\d{4})\s(\d{2}):(\d{2}):(\d{2})\s([\+\-])(\d{2})(\d{2})', t)

        times[i] = {'day' : tdata.group(1),
                       'date': tdata.group(2),
                       'month': tdata.group(3),
                       'year': tdata.group(4),
                       'h': tdata.group(5),
                       'm': tdata.group(6),
                       's': tdata.group(7),
                       'dH' : tdata.group(9),
                       'dM': tdata.group(10)
                       }

    return times





x = 'Sat 02 May 2015 19:54:36 +0530'
y = 'Fri 01 May 2015 13:54:36 -0000'

time_delta(x, y)