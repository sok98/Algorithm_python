def solution(s):
    answer = ""
    eng_num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    check = ""
    for i in s:
        if i.isdigit():  # 숫자일 때
            answer += str(i)
        else:  # 알파벳일 때
            check += i
            if check in eng_num:  # 맞는 숫자있는지 확인
                answer += str(eng_num[check])
                check = ""  # 초기화

    return int(answer)


print(solution("one4seveneight"))
