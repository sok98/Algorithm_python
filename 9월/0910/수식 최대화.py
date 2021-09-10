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
                if o == '*':
                    calcul[i] = int(calcul[i-1]) * int(calcul[i+1])
                    del calcul[i-1]
                    del calcul[i]
                elif o == '+':
                    calcul[i] = int(calcul[i-1]) + int(calcul[i+1])
                    del calcul[i-1]
                    del calcul[i]
                elif o == '-':
                    calcul[i] = int(calcul[i-1]) - int(calcul[i+1])
                    del calcul[i-1]
                    del calcul[i]
        answer = max(answer, (abs(calcul[0])))

    return answer