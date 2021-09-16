def solution(n, z, roads, queries):
    answer = []
    for c in queries:
        current = 0
        move = 0
        while c != current:
            move += 1
        answer.append(move)
    return answer


print(solution(5, 5, [[1, 2, 3], [0, 3, 2]], [0]))
