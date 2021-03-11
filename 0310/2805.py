import math

N, M = map(int, input().split())
tree = list(map(int, input().split()))

min = 1000000000
sum = 0
for i in tree:
    sum += i
    if i < min:
        min = i

temp = (sum - (min * N)) - M
if temp < 0:
    print(min - math.ceil(-temp / N))
elif temp == 0:
    print(min)
else:
    print(min + (temp // (N-tree.count(min))))


#print((sum-(min*N)-M) / tree.count(not min))
