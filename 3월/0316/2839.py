N = int(input())

if N % 5 % 3 != 0:
    result = -1
    for i in range(N // 5):
        d = N % 5 + 5 * (i+1)
        if d % 3 == 0:
            result = N // 5 - (i+1) + d / 3
            break
    print(int(result))
else:
    print(int(N // 5 + N % 5 / 3))
