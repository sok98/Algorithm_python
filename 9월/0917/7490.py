from itertools import product
import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    N = int(input())
    result = []

    for insert in product(['+', '-', ' '], repeat=N-1):
        num = 1
        expression = '1'
        for i in insert:
            num += 1
            expression += i + str(num)
        
        if eval(expression.replace(' ', '')) == 0:
            result.append(expression)

    answer.append(sorted(result))

for result in answer:
    for r in result:
        print(r)
    print()