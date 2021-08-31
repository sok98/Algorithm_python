import sys
input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))
n.sort()

M = int(input())
m = list(map(int, input().split()))

def search(x, start, end) :
    while start <= end:
        mid = (start+end) // 2
        if x == n[mid]:
            return 1
        elif x < n[mid]:
            end =  mid - 1
        elif x > n[mid]:
            start = mid + 1
    return 0

for i in m:
    print(search(i, 0, N-1))