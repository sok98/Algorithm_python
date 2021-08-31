import sys
input = sys.stdin.readline

N, M = map(int, input().split())

password = {}
for _ in range(N):
    site, p = input().split()
    password[site] = p

for _ in range(M):
    print(password[input().strip()])
