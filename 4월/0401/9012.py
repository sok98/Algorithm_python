import sys
T = int(sys.stdin.readline())

answer = []
for i in range(T):
    vps = list(input())
    stack = []
    a = "YES"
    for n in vps:
        if n == ")":
            if not stack:
                a = "NO"
                break
            ps = stack.pop()

        else:
            stack.append(n)
    if stack:
        a = "NO"
    answer.append(a)


for i in answer:
    print(i)
