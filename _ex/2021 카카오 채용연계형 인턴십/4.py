def solution(n, start, end, roads, traps):
    answer = []
    con = {i: [] for i in range(1, n+1)}
    con_trap = {i: [] for i in range(1, n + 1)}
    trap = False

    for r in roads:
        con[r[0]].append([r[1], r[2]])
        con_trap[r[1]].append([r[0], r[2]])

    sum = 0

    def search(p, sum):
        sum += p[1]

        if p[0] == end or (len(answer) != 0 and sum > min(answer)):
            answer.append(sum)
            return

        if p[0] in traps:
            con[p[0]], con_trap[p[0]] = con_trap[p[0]], con[p[0]]
        for i in con[p[0]]:
            search(i, sum)

    search([start, 0], 0)

    return min(answer)


#print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
