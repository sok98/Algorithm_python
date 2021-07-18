def solution(record):
    answer = []
    name = {}

    info_list = []
    for re in record:
        info = list(re.split(" "))
        info_list.append(info)
        if info[0] != "Leave":
            name[info[1]] = info[2]

    for i in info_list:
        if i[0] == "Enter":
            answer.append(name[i[1]]+"님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(name[i[1]]+"님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
