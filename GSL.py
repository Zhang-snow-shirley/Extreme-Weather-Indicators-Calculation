import csv
import datetime
import pandas as pd
import numpy as np
import math

file_path = './'


def get_date_range(begin_time, end_time):
    date_list = []
    while begin_time <= end_time:  # 当begin日期小于end日期执行以下
        date_list.append(begin_time)  # 返回日期列表
        begin_date_object = datetime.datetime.strptime(begin_time, "%Y-%m-%d")  # 设定日期格式
        days1_timedelta = datetime.timedelta(days=1)
        begin_time = (begin_date_object + days1_timedelta).strftime("%Y-%m-%d")
    return date_list


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
    return np.array(total_low).T, np.array(total_high).T, total_count


def write_file(data, file_type, begin_time, end_time):
    out_file = file_path + file_type + begin_time + '-' + end_time + '.csv'
    header = ["id", file_type]
    with open(out_file, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(1, len(data) + 1):
            writer.writerow([i, data[i - 1]])

            
def growing_season_length(nums, n):
    start, end = None, None
    for i in range(len(nums)-5):
        if all(n > 5 for n in nums[i:i+6]):
            start = i + 6
            break
    if start is None:
        return 0, 0
    for i in range(start+len(nums[start:])-5):
        if all(n < 5 for n in nums[i:i+6]) and i > n:
            end = i + 5
            break
    if end is None:
        return start, len(nums)
    else:
        return start, end


if __name__ == '__main__':
    begin_date = "2000-06-10"
    end_date = "2000-06-30"
    begin_date_object = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    july_1st = datetime.datetime.strptime("2000-07-01", "%Y-%m-%d")
    delta_time = max((july_1st - begin_date_object).days, 0)
    low_temp, high_temp, count = read_file(begin_date, end_date)
    average = (low_temp + high_temp) / 2
    diff = (high_temp - low_temp) / 2
    growing_days, average_day_temp, average_day_diff = [], [], []
    for i in range(len(average)):
        num = average[i]
        dif = diff[i]
        start_i, end_i = growing_season_length(num, delta_time)
        if start_i < end_i:
            growing_days.append(end_i - start_i)
            average_day_temp.append(np.mean(num[start_i:end_i+1]))
            average_day_diff.append(np.mean(dif[start_i:end_i+1]))
        else:
            growing_days.append(0)
            average_day_temp.append('nan')
            average_day_diff.append('nan')
    write_file(growing_days, 'growing_days', begin_date, end_date)
    write_file(average_day_temp, 'average_day_temp', begin_date, end_date)
    write_file(average_day_diff, 'average_day_diff', begin_date, end_date)