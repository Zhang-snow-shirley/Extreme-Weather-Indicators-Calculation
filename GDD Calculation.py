#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import datetime
import pandas as pd
import numpy as np
import math

file_path = 'E:/2000年气温数据/'#enter the workplace

def get_date_range(begin_time, end_time):
    date_list = []
    while begin_time <= end_time:  
        date_list.append(begin_time)  
        begin_date_object = datetime.datetime.strptime(begin_time, "%Y-%m-%d")  # set the date form
        days1_timedelta = datetime.timedelta(days=1)
        begin_time = (begin_date_object + days1_timedelta).strftime("%Y-%m-%d")
    return date_list


def average_method(low, high, base_temp):
    res = [(h + l) / 2 - base_temp for h, l in zip(high, low)]
    res = np.array(res)
    res[res < 0] = 0
    out = np.sum(res, axis=0) / len(res)
    return out


def cal_area(h, l, base_temp):
    #积分计算曲线面积
    xarr = []
    yarr = []
    num = 100
    for i in range(num):
        xarr.append(math.pi / num * i)
    for j in xarr:
        func = (h - l) * math.sin(j) + l - base_temp
        func[func < 0] = 0
        yarr.append(func * math.pi / num)
    res = sum(yarr)
    return res


def BE_method(low, high, base_temp):
    GDD_BE = []
    for h, l in zip(high, low):
        GDD_BE.append(cal_area(h, l, base_temp))
    return sum(GDD_BE) / len(GDD_BE)


def read_file(begin_time, end_time):
    date_list = get_date_range(begin_time, end_time)
    total_low = []
    total_high = []
    total_count = 0
    for date in date_list:
        low = pd.read_csv(file_path + '2000年日最低气温/file' + date + '.csv', header=0, names=["pointid", "low"])
        high = pd.read_csv(file_path + '2000年日最高气温/file' + date + '.csv', header=0, names=["pointid", "high"])
        total_low.append(low["low"].values)
        total_high.append(high["high"].values)
        total_count += 1
    return np.array(total_low), np.array(total_high), total_count


def write_file(gdd, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'GDD.csv'
    header = ["id", "GDD"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, len(gdd) + 1):
            writer.writerow([i, gdd[i - 1]])

#enter begin_date、end_date and base_temp to calculate GDD in 2 methods
if __name__ == '__main__':
    begin_date = "2000-10-25"
    end_date = "2000-11-05"
    base_temp = 10
    low_temp, high_temp, count = read_file(begin_date, end_date)
    GDD_aver = average_method(low_temp, high_temp, base_temp)
    GDD_BE = BE_method(low_temp, high_temp, base_temp)
    write_file(GDD_aver, "aver", begin_date, end_date)
    write_file(GDD_BE, "BE", begin_date, end_date)


# In[ ]:




