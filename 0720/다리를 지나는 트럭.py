from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    if sum(truck_weights) <= weight:
        return bridge_length + len(truck_weights)
    
    truck_weights = deque(truck_weights)    # 트럭 별 무게 리스트 deque로 변경
    on_bridge = deque([0]*bridge_length)    # 다리에 올라갈 수 있는 트럭 수 만큼 deque 생성
    cnt_time = 0    # 시계
    sum_weight = 0  # 다리에 올라와있는 트럭 무게 합

    while truck_weights:    # 올라갈 트럭이 남아 있다면
        cnt_time += 1   # 시간 증가
        out = on_bridge.popleft()
        sum_weight -= out
        if sum_weight + truck_weights[0] <= weight:  # 다리에 트럭이 올라갈 수 있으면
            truck = truck_weights.popleft()
            on_bridge.append(truck) # 다리에 트럭 추가
            sum_weight += truck     # 트럭 무게 합 추가
        else:
            on_bridge.append(0)

    return cnt_time + bridge_length # 마지막 트럭 다 지나가는 시간 bridge_length 더하기



print(solution(2,10,[7,4,5,6]))