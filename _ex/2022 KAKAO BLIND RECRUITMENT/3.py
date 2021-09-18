import math

def solution(fees, records):
    cars = {}
    
    for re in records:
        time, car, io = re.split()
        h, m = time.split(":")
        time = int(h)*60 + int(m)
        
        if io == "IN":
            if car in cars:
                cars[car][1] = time
            else:
                cars[car] = [0, time]
        else:   # OUT
            cars[car][0] += time - cars[car][1]
            cars[car][1] = -1
            
    last_time = 23*60 + 59
    for car in cars.values():
        if car[1] != -1:
            car[0] += last_time - car[1]
            car[1] = -1
        
        if car[0] > fees[0]:
            car[0] = fees[1] + math.ceil((car[0] - fees[0]) / fees[2]) * fees[3]
        else:
            car[0] = fees[1]
            
    return [ x[1][0] for x in sorted(cars.items())]