import sys
input = sys.stdin.readline

target = input().strip()
bump = list(input().strip())
length = len(bump)

stack = []
for c in target:
    stack += c
    if stack[-length:] == bump:
        for _ in range(length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
