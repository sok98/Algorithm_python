line = []
start = ["(", "["]

line.append(input())
while line[-1] != ".":
    line.append(input())


def search(k, s):
    p = "#"
    while p != start[k]:
        if not s or p == start[(k+1) % 2]:
            global result
            result = "no"
            return
        p = s.pop()


stack = []
for i in line[:-1:]:
    result = "yes"
    for n in range(len(i)):
        if i[n] == ")":
            search(0, stack)
        elif i[n] == "]":
            search(1, stack)
        else:
            stack.append(i[n])

        if not stack:
            break
    print(result)
