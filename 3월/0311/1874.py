n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

stack = []
result = []
k = 0


def s_pop(s):
    global k
    while n > k and stack and numbers[k] == s[-1]:
        s.pop()
        result.append("-")
        k += 1


for i in range(1, n+1):
    stack.append(i)
    result.append("+")
    if numbers[k] == stack[-1]:
        s_pop(stack)

if n > k:
    print("NO")
else:
    for i in result:
        print(i)
