#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#导入需要的包
import csv
import datetime
import pandas as pd
import numpy as np
import math


# In[ ]:


file_path = 'E:/2000年气温数据/'#在此处写入工作路径


# In[ ]:


#日期获取
def get_date_range(begin_time, end_time):
    date_list = []
    while begin_time <= end_time:  # 当begin日期小于end日期执行以下
        date_list.append(begin_time)  # 返回日期列表
        begin_date_object = datetime.datetime.strptime(begin_time, "%Y-%m-%d")  # 设定日期格式
        days1_timedelta = datetime.timedelta(days=1)
        begin_time = (begin_date_object + days1_timedelta).strftime("%Y-%m-%d")
    return date_list


# In[ ]:


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


# In[ ]:


def txx_find(high_temp):
    txx = []
    for j in range(97115):
        largest_so_far=None  
        for i in high_temp:
            if largest_so_far==None:
                largest_so_far=i[j]
            elif i[j]>largest_so_far:
                largest_so_far=i[j]        
        txx.append(largest_so_far)
    return txx


# In[ ]:


def tnx_find(low_temp):
    tnx = []
    for j in range(97115):
        largest_so_far=None  
        for i in low_temp:
            if largest_so_far==None:
                largest_so_far=i[j]
            elif i[j]>largest_so_far:
                largest_so_far=i[j]        
        tnx.append(largest_so_far)
    return tnx


# In[ ]:


def txn_find(high_temp):
    txn = []
    for j in range(97115):
        smallest_so_far=None  
        for i in high_temp:
            if smallest_so_far==None:
                smallest_so_far=i[j]
            elif i[j]<smallest_so_far:
                smallest_so_far=i[j]        
        txn.append(smallest_so_far)
    return txn


# In[ ]:


def tnn_find(low_temp):
    tnn = []
    for j in range(97115):
        smallest_so_far=None  
        for i in low_temp:
            if smallest_so_far==None:
                smallest_so_far=i[j]
            elif i[j]<smallest_so_far:
                smallest_so_far=i[j]        
        tnn.append(smallest_so_far)
    return tnn


# In[ ]:


def write_file(txx, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'TXx.csv'
    header = ["id", "txx"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 97115):
            writer.writerow([i, txx[i - 1]])


# In[ ]:


def write_file(txn, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'TXn.csv'
    header = ["id", "txn"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 97115):
            writer.writerow([i, txn[i - 1]])


# In[ ]:


def write_file(tnx, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'TNx.csv'
    header = ["id", "tnx"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 97115):
            writer.writerow([i, tnx[i - 1]])


# In[ ]:


def write_file(tnn, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + 'TNn.csv'
    header = ["id", "tnn"]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, 97115):
            writer.writerow([i, tnn[i - 1]])


# In[ ]:


if __name__ == '__main__':
    begin_date = "2000-01-01"
    end_date = "2000-12-31"
    low_temp, high_temp, count = read_file(begin_date, end_date)
    txx=txx_find(high_temp)
    txn=txn_find(high_temp)
    tnx=tnx_find(low_temp)
    tnn=tnn_find(low_temp)
    write_file(txx, "annual", begin_date, end_date)
    write_file(txn, "annual", begin_date, end_date)
    write_file(tnx, "annual", begin_date, end_date)
    write_file(tnn, "annual", begin_date, end_date)

