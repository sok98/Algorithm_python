def solution(clothes):
    kinds = {}
    for i in clothes:
        if i[1] in kinds:
            kinds[i[1]] += 1
        else:
            kinds[i[1]] = 2

    answer = 1
    for j in kinds.values():
        answer *= j

    return answer-1
