n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

stack = []
result = []
k = 0


def s_pop(s):
    s.pop()
    result.append("-")
    global k
    k += 1
   # print("testtesttest: ", numbers[k], s[-1])
    if n > k and numbers[k] == s[-1]:
        s_pop(s)


for i in range(1, n+1):
    print("aaaaaaaa: ", i)
    stack.append(i)
    result.append("+")
    if numbers[k] == stack[-1]:
        s_pop(stack)

print(result)
