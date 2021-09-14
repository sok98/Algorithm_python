import math
A, B, V = map(int, input().split())
days = 1
if V > A:
    days += math.ceil((V-A)/(A-B))
print(days)
