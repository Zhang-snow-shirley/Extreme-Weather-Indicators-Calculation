#!/usr/bin/env python
# coding: utf-8

# In[104]:


#导入需要的包
import csv
import datetime
import pandas as pd
import numpy as np
import math


# In[105]:


file_path = 'E:/2000年气温数据/'#在此处写入工作路径


# In[106]:


#日期获取
def get_date_range(begin_time, end_time):
    date_list = []
    while begin_time <= end_time:  # 当begin日期小于end日期执行以下
        date_list.append(begin_time)  # 返回日期列表
        begin_date_object = datetime.datetime.strptime(begin_time, "%Y-%m-%d")  # 设定日期格式
        days1_timedelta = datetime.timedelta(days=1)
        begin_time = (begin_date_object + days1_timedelta).strftime("%Y-%m-%d")
    return date_list


# In[107]:


#读取文件
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


# In[111]:


def fd0_count(low_temp):
    fd0 = []
    for j in range(97115):
        count=0
        for i in low_temp:
            if i[j]<0:
                count=count+1
        fd0.append(count)
    return fd0


# In[ ]:


def id0_count(high_temp):
    id0 = []
    for j in range(97115):
        count=0
        for i in high_temp:
            if i[j]<0:
                count=count+1
        id0.append(count)
    return id0


# In[ ]:


def sud25_count(high_temp):
    sud25 = []
    for j in range(97115):
        count=0
        for i in high_temp:
            if i[j]>25:
                count=count+1
        sud25.append(count)
    return sud25


# In[ ]:


def tr20_count(low_temp):
    tr20 = []
    for j in range(97115):
        count=0
        for i in low_temp:
            if i[j]>20:
                count=count+1
        tr20.append(count)
    return tr20


# In[112]:


def write_file(fd0, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'FD0.csv'
    header = ["id", "FD0"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 97115):
            writer.writerow([i, fd0[i - 1]])


# In[ ]:


def write_file(id0, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'ID0.csv'
    header = ["id", "ID0"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 97115):
            writer.writerow([i, id0[i - 1]])


# In[ ]:


def write_file(sud25, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'SUD25.csv'
    header = ["id", "SUD25"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 97115):
            writer.writerow([i, sud25[i - 1]])


# In[ ]:


def write_file(tr20, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'TR20.csv'
    header = ["id", "TR20"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 97115):
            writer.writerow([i, tr20[i - 1]])


# In[114]:


if __name__ == '__main__':
    begin_date = "2000-01-01"
    end_date = "2000-12-31"
    low_temp, high_temp, count = read_file(begin_date, end_date)
    fd0=fd0_count(low_temp)
    write_file(fd0, "annual", begin_date, end_date)


# In[ ]:


if __name__ == '__main__':
    begin_date = "2000-01-01"
    end_date = "2000-12-31"
    low_temp, high_temp, count = read_file(begin_date, end_date)
    id0=id0_count(high_temp)
    write_file(id0, "annual", begin_date, end_date)


# In[ ]:


if __name__ == '__main__':
    begin_date = "2000-01-01"
    end_date = "2000-12-31"
    low_temp, high_temp, count = read_file(begin_date, end_date)
    sud25=sud25_count(high_temp)
    write_file(sud25, "annual", begin_date, end_date)


# In[ ]:


if __name__ == '__main__':
    begin_date = "2000-01-01"
    end_date = "2000-12-31"
    low_temp, high_temp, count = read_file(begin_date, end_date)
    tr20=tr20_count(low_temp)
    write_file(tr20, "annual", begin_date, end_date)

