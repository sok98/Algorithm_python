T = int(input())
case = []
for t in range(T):
    case.append(int(input()))

P = [1, 1, 1, 2, 2]
for i in range(100):
    P.append(P[-1] + P[i])

for c in case:
    print(P[c-1])
