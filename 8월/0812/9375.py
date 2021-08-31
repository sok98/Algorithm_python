import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    case = {}
    for _ in range(n):
        c = list(input().split())
        if c[1] in case:
            case[c[1]] += 1
        else:
            case[c[1]] = 2  # 0인 경우, 1인 경우 -> 2개
    answer = 1
    for cnt in case.values():
        answer *= cnt
    print(answer-1)