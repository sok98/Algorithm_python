def solution(a, edges):
    answer = 0

    dic = {}
    for i in range(len(a)):
        dic[i] = a[i]

    con = {}
    for i in edges:
        if i[0] in con:
            con[i[0]].append(i[1])
        else:
            con[i[0]] = [i[1]]
        if i[1] in con:
            con[i[1]].append(i[0])
        else:
            con[i[1]] = [i[0]]

    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
