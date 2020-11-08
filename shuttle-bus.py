#https://programmers.co.kr/learn/courses/30/lessons/17678

def stamp2time(stamp):
    return int(stamp[:2])*60 + int(stamp[-2:])

def time2stamp(time):
    h, m = divmod(time, 60)
    return f'{h:02d}' + ':' + f'{m:02d}'

def solution(n, t, m, timetable):
    firstbustime = 540 #09:00
        
    arr_times = [None]*n
    for i in range(n): arr_times[i] = list()
    
    for timestamp in timetable:
        time = stamp2time(timestamp)
        tt = (firstbustime - time) // t
        
        if (tt>=0):
            arr_times[0].append(time)
        elif (tt > -n): # -n+1 ~ -1
            arr_times[-tt].append(time)
    
    for i in range(n): arr_times[i].sort()
    
    waitq = []
    
    for i in range(n-1):
        waitq += arr_times[i]
        waitq = waitq[m:]
    waitq += arr_times[n-1]
    
    if len(waitq)<m:
        return time2stamp(firstbustime + (n-1)*t)
    else:
        return time2stamp(waitq[m-1]-1)

