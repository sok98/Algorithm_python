def solution(n, computers):
    answer = 0
    graph = {}
    for i in range(n):
        graph[i] = list(filter(lambda x: computers[i][x] == 1, range(n)))

    visited = []
    for i in range(n):
        if i not in visited:
            # DFS
            stack = [i]
            while stack:
                k = stack.pop()
                if k not in visited:
                    visited.append(k)
                    stack.extend(graph[k])

            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
