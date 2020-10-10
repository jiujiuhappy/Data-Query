import datetime

def GetAllTime(start,end):
    '''给出起始和终止日期，获取之间所有日期，并返回日期列表'''
    datestart = datetime.datetime.strptime(start, '%Y/%m/%d')
    dateend = datetime.datetime.strptime(end, '%Y/%m/%d')
    day = [datestart.strftime('%Y/%m/%d')]

    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        day.append(datestart.strftime('%Y/%m/%d'))

    return day # 返回一个日期列表

if __name__ == '__main__':
    day = GetAllTime('2016-1-1' ,'2016-01-03')
    print(day)