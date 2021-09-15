from collections import deque

def solution(enter, leave):
    answer = [0 for _ in range(len(enter)+1)]
    leave = deque(leave)
    
    room = []
    for i in enter:
        # 원래 있던 숫자랑 만남 표시
        if room:
            answer[i] += len(room)
            for r in room:
                answer[r] += 1
        room.append(i)

        while room and leave and leave[0] in room:
            room.remove(leave[0])
            leave.popleft()
    
    return answer[1:]