def solution(info, edges):
    
    graph = {i:[] for i in range(len(info))}
    re_graph = {i:0 for i in range(len(info))}
    for a, b in edges:
        graph[a].append(b)
        re_graph[b] = a
        
    count = {i:[set(), set()] for i in range(len(info))}
    count[0][info[0]].add(0)
    stack = [0]

    
    while stack:
        n = stack.pop()
        for i in graph[n]:  # i = 나 / n = 전(re_graph[i])
            count[i][0] = count[n][0].copy()
            count[i][1] = count[n][1].copy()
            count[i][info[i]].add(i)
            stack.append(i)

    answer = [[set(), set()], 0]
    sheep = [i for i in range(len(info)) if info[i] == 0]
    sheep = sorted(sheep, key=lambda x:len(count[x][0]), reverse=True)
    for s in sheep:
        if s not in answer[0]:
            candidate = [answer]
            
            if len(count[s][0])-len(count[s][1]) > 0:
                candidate.append([count[s], len(count[s][0])])
            
            combi_set = [count[s][0]|answer[0][0], count[s][1]|answer[0][1]]
            if len(combi_set[0])-len(combi_set[1]) > 0:
                candidate.append([combi_set, len(combi_set[0])])
            
            answer = sorted(candidate, key=lambda x:x[1], reverse=True)[0]

    return len(answer[0][0])