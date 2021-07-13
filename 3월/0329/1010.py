import math
T = int(input())
answer = []
for i in range(T):
    N, M = map(int, input().split())
    answer.append(math.factorial(M)//math.factorial(N)//math.factorial(M-N))

for i in answer:
    print(i)
