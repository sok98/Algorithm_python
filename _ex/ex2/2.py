from collections import deque


def solution(s):
    s = deque(s)
    answer = 0
    find = {')': '(', ']': '[', '}': '{'}

    for i in range(len(s)):

        stack = []
        result = True
        for n in s:
            if n in find.values():
                stack.append(n)
            elif n in find:
                if stack and stack[-1] == find[n]:
                    stack.pop()
                else:
                    result = False
                    break
        if stack:
            result = False
        if result == True:
            answer += 1
        s.rotate(-1)

    return answer


print(solution("[](){}"))
