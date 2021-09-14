case = []
case.append(int(input()))
while case[-1] != 0:
    case.append(int(input()))
del case[-1]

numbers = [True for i in range((max(case) * 2)+1)]
numbers[0] = False
numbers[1] = False

for i in range(2, int(len(numbers)**0.5+1)):
    if numbers[i]:
        for n in range(i**2, len(numbers), i):
            numbers[n] = False

for n in case:
    result = 0
    for t in range(n+1, (n * 2)+1):
        if numbers[t] == True:
            result += 1
    print(result)
