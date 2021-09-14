import math
T = int(input())
result = []
for t in range(T):
    a, b = list(map(int, input().split()))
    result.append(math.lcm(a, b))

for m in result:
    print(m)
