from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    default_out = 23 * 60 + 59
    for record in records:
        time, num, in_out = record.split()
        minute = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
        if in_out == "IN":
            cars[num].append(default_out - minute)
        elif in_out == "OUT":
            cars[num][-1] -= (default_out - minute)
    
    cars = dict(sorted(cars.items()))
    
    times = []
    for car in cars:
        times.append(sum(cars[car]))
    
    for time in times:
        if time > fees[0]:
            answer.append(fees[1] + (math.ceil((time-fees[0])/fees[2])) * fees[3])
        else:
            answer.append(fees[1])       
    
    return answer