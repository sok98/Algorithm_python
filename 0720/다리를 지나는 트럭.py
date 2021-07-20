from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    if sum(truck_weights) <= weight:
        return bridge_length + len(truck_weights)
    
    truck_weights = deque(truck_weights)
    on_bridge = deque([0]*bridge_length)
    cnt_time = 0
    sum_weight = 0

    while truck_weights:
        cnt_time += 1
        sum_weight -= on_bridge.popleft()
        if sum(on_bridge) + truck_weights[0] < weight:
            pop = truck_weights.popleft()
            on_bridge.append(pop)
            sum_weight += pop
        else:
            on_bridge.append(0)

    return cnt_time + bridge_length

print(solution(2,10,[7,4,5,6]))