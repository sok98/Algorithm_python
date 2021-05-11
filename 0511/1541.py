import sys
input = sys.stdin.readline

exp = input()
num = ""
sign = "+"
answer = 0

minus = False
for i in exp:
    if i.isdigit():  # 숫자일 때
        num += i
    else:           # 숫자 끝
        num = int(num)

        if sign == "-":
            minus = True
            answer -= num

        elif sign == "+":
            if minus == True:   # 괄호 안
                answer -= num
            else:               # 괄호 밖
                answer += num

        sign = i    # + 또는 - 저장
        num = ""    # num 초기화


print(answer)
