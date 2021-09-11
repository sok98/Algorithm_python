from itertools import permutations

def solution(expression):
    answer = 0
    expression = expression.replace("-", " - ").replace("+", " + ").replace("*", " * ").split()
    operator = [i for i in ['*', '+', '-'] if i in expression]
    
    for op in permutations(operator, len(operator)):
        calcul = expression.copy()
        for o in op:
            while o in calcul:
                i = calcul.index(o)
                calcul = calcul[:i-1] + [str(eval(''.join(calcul[i-1:i+2])))] + calcul[i+2:]
        answer = max(answer, (abs(int(calcul[0]))))

    return answer