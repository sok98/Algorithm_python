import sys
from collections import deque
N = int(sys.stdin.readline())


def pop():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())


def size():
    print(len(queue))


def empty():
    if not queue:
        print(1)
    else:
        print(0)


def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])


def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])


d = {"pop": pop, "size": size, "empty": empty, "front": front, "back": back}

queue = deque([])
for i in range(N):
    cmd = sys.stdin.readline()
    if "push" in cmd:
        x = list(cmd.split())
        queue.append(x[1])
    else:
        d[cmd[:-1]]()
