N = int(input())
check = 0
for i in range(N):
    word = input()
    new = []
    before = "_"
    for j in word:
        if j not in new:
            new.append(j)
        elif before != j and j in new:
            check += 1
            break
        before = j


print(N-check)
