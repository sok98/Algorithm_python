import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = input()
uvw = [input().split() for _ in range(E)]
# for _ in range(E):
#     uvw.append(input().split())

print(uvw)
