def solution(n, k, cmd):
    answer = {i: "O" for i in range(n)}
    point = k

    stack = []
    for i in cmd:
        if "U" in i:  # 위로 i[2]칸
            count = int(i[2])
            while count > 0:
                point -= 1
                if answer[point] == "O":
                    count -= 1

        elif "D" in i:  # 아래로 i[2]칸
            count = int(i[2])
            while count > 0:
                point += 1
                if answer[point] == "O":
                    count -= 1

        elif i == "C":  # 삭제
            answer[point] = "X"
            stack.append(point)
            if point == n - 1:  # 마지막 행이였을 경우 위로 한칸
                point -= 1
            else:
                point += 1

        elif i == "Z":  # 복구
            answer[stack.pop()] = "O"
    result = ""
    for i in range(n):
        result += answer[i]
    return result

    # elif i == "C":  # 삭제
    #     stack.append([point, table[point]])
    #     answer[table[point]] = "X"
    #     del table[point]
    #     # 삭제된 행이 가장 마지막 행인 경우 윗 행 선택
    #     if point >= len(table):
    #         point = len(table) - 1

    # elif i == "Z":  # 복구
    #     pop = stack.pop()
    #     answer[pop[1]] = "O"
    #     table.insert(pop[0], pop[1])
    #     if pop[0] <= point:
    #         point += 1


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
