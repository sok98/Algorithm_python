import sys
input = sys.stdin.readline

N = int(input())

N = sorted(str(N), reverse = True)

print(''.join(N))