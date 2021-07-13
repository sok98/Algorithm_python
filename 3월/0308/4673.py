N = 10000
selfie = [False for i in range(N+1)]


def digit_hap(num):
    s = num
    while num > 0:
        s += num % 10
        num = num//10
    return s


for i in range(1, N+1):
    if selfie[i] == False:
        move = i
        while True:
            if move < 10:
                move = 2*move
            else:
                move = digit_hap(move)
            if move > N:
                break
            selfie[move] = True

for idx, value in enumerate(selfie):
    if value == False and idx != 0:
        print(idx)
