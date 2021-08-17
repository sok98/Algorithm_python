import sys
input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)

else:
    for i in range(N-1, 0, -1):
        N *= i

    for idx, n in enumerate("".join(reversed(str(N)))):
        if n != '0':
            print(idx)
            break