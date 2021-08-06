from collections import deque

n = int(input())
switch = deque(map(int, input().split(" ")))
switch.append(0)
switch.rotate(1)

def change(n) :
    if switch[n] == 0:
        switch[n] = 1
    else:
        switch[n] = 0

s = int(input())
for _ in range(s):
    gender, num = map(int, input().split(" "))

    if gender == 1: # 남학생
        i = 1
        target = num * i
        while target < len(switch):
            change(target)
            i += 1
            target = num * i

    else:   # 여학생
        change(num)
        i = 1
        while num-i >= 0 and num+i < len(switch) and switch[num-i] == switch[num+i]:
            change(num-i)
            change(num+i)
            i += 1

switch.popleft()
if len(switch) > 20:
    i = 0
    while i+20 < len(switch):
        for i in switch[i, i+20]:
            print(i, end=" ")
        i += 1
else:
    for i in switch:
        print(i, end=" ")
