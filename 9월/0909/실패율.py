def solution(N, stages):
    answer = {}

    stages = sorted(stages)
    users = len(stages)

    for i in range(1,N+1):
        if i in stages:
            answer[i] = stages.count(i) / (users - stages.index(i))
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x:answer[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))