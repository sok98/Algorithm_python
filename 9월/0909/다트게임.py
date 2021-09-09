def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k')
    squared = { 'S':1, 'D':2, 'T':3 }
    
    for n in dartResult:
        if n in squared:
            answer[-1] = answer[-1]**squared[n]
        elif n == '#':
            answer[-1] *= -1
        elif n == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer [-2] *= 2
        elif n == 'k':
            answer.append(10)
        else:
            answer.append(int(n))

    return sum(answer)