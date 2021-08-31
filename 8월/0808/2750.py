import sys
input = sys.stdin.readline

N = int(input())

number = []
for _ in range(N):
    number.append(int(input()))

number.sort()
for i in number:
    print(i)