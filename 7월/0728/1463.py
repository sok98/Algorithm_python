import sys
from collections import defaultdict

number = int(sys.stdin.readline())
count = defaultdict(lambda : 999999)
count[1], count[2], count[3] = 0, 1, 1

for n in range(4, number+1):
    if n%3 == 0 and n%2 == 0:
        count[n] = min(count[n//3], count[n//2], count[n-1]) + 1
    elif n%3 == 0:
        count[n] = min(count[n//3], count[n-1]) + 1
    elif n%2 == 0:
        count[n] = min(count[n//2], count[n-1]) + 1
    else:
        count[n] = count[n-1] + 1

print(count[number])