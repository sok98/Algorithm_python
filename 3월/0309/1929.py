M, N = map(int, input().split())

number = [True for i in range(N+1)]

for i in range(2, int(N**0.5)+1):
    if number[i]:
        for j in range(2*i, N+1, i):
            number[j] = False

for index in range(M, N+1):
    if number[index] and index != 1:
        print(index)
