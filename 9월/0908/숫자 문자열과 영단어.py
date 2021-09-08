def solution(s):
    answer = ""
    numbers = { "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 }
    check = ""
    for i in s:
        if i.isdigit():
            answer += str(i)
        else:
            check += i
            if check in numbers:
                answer += str(numbers[check])
                check = ""
    return int(answer)


# 다른풀이
# def solution(s):
#     numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     for i, n in enumerate(numbers):
#         s = s.replace(n, str(i))

#     return int(s)