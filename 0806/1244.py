import sys
input = sys.stdin.readline

change = {1:0, 0:1}

n = int(input())
switch = list(map(int, input().split()))
s = int(input())

for _ in range(s):
    g, num = map(int, input().split())
    if g == 1: # 남학생
        target = num-1
        while target < n:
            switch[target] = change[switch[target]]
            target += num

    else:   # 여학생
        num -= 1
        switch[num] = change[switch[num]]
        i = 1
        while num-i >= 0 and num+i < n and switch[num-i] == switch[num+i]:
            switch[num-i] = change[switch[num-i]]
            switch[num+i] = change[switch[num+i]]
            i += 1

for i in range(0, n, 20):
    print(*switch[i:i+20])