from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    if sum(truck_weights) <= weight:
        return bridge_length + len(truck_weights)

    on_bridge = deque([0]*bridge_length)
    cnt_time = 0
    i = 0
    while i < len(truck_weights):
        cnt_time += 1
        on_bridge.popleft()
        if sum(on_bridge) + truck_weights[i] < weight:
            on_bridge.append(truck_weights[i])
            i += 1
        else:
            on_bridge.append(0)

    return cnt_time + bridge_length

print(solution(2,10,[7,4,5,6]))