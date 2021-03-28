T = int(input())
answer = []
for i in range(T):
    x, y = map(int, input().split())
    i = 1
    while True:
        if y - x <= i*i:
            answer.append(i+i-1)
            break
        if y - x <= i * i + i:
            answer.append(i + i)
            break
        i += 1


for i in answer:
    print(i)
