import sys
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    cmd = sys.stdin.readline()

    # 정수를 스택에 넣는 연산
    if "push" in cmd:
        x = list(cmd.split())
        stack.append(x[1])

    # 스택에서 가장 위에 정수를 빼고 출력, 없는 경우 -1
    elif "pop" in cmd:
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    # 스택에 들어있는 정수의 개수 출력
    elif "size" in cmd:
        print(len(stack))

    # 스택이 비어있으면 1, 아니면 0
    elif "empty" in cmd:
        if not stack:
            print(1)
        else:
            print(0)

    # 스택의 가장 위에 있는 정수 출력, 없는 경우 -1
    elif "top" in cmd:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
