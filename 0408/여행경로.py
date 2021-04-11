def solution(tickets):

    tickets.sort(reverse=True)
    graph = dict()
    for t in tickets:
        if t[0] not in graph:
            graph[t[0]] = [t[1]]
        else:
            graph[t[0]].append(t[1])

    stack = ["ICN"]
    visited = []

    while stack:
        n = stack[-1]
        if n not in graph or len(graph[n]) == 0:
            visited.append(stack.pop())
        else:
            stack.append(graph[n][-1])
            graph[n] = graph[n][:-1]

    return visited[::-1]
