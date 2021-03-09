for i in range(int(input())):
    H, W, N = map(int, input().split())

    if N % H == 0:
        x = N//H
        y = H
    else:
        x = N//H + 1
        y = N % H

    print(y*100+x)
