line = []
find = {')': '(', ']': '['}

line.append(input())
while line[-1] != ".":
    line.append(input())

for i in line[:-1:]:
    result = "yes"
    stack = []
    for n in i:
        if n in find.values():  # (, [ 가 들어올 때
            stack.append(n)
        elif n in find:  # ), ] 가 들어올 때
            if stack and stack[-1] == find[n]:  # stack의 마지막 값이 내 짝이라면
                stack.pop()
            else:
                result = "no"
                break
    if stack:   # stack에 ( 나 [가 있는 상태로 끝났을 때
        result = "no"
    print(result)
