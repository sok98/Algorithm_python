from collections import deque
N, M = map(int, input().split())
number = list(map(int, input().split()))
answer = 0

deq = deque()
for i in range(1, N + 1):
    deq.append(i)

for n in number:
    idx = deq.index(n)
    if idx == 0:
        deq.popleft()
    else:
        if idx < len(deq) - idx:
            answer += idx
            deq.rotate(-idx)
            deq.popleft()
        else:
            answer += len(deq) - idx
            deq.rotate(len(deq) - idx)
            deq.popleft()

print(answer)
