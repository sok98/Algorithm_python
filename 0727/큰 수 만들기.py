def solution(number, k):
    # answer = ''

    # # max 함수
    # def _max(s, e):
    #     num = [s, number[s]]
    #     for i in range(s, e):
    #         if number[i] == "9":
    #             return [i, 9]
    #         elif number[i] > num[1]:
    #             num = [i, number[i]]
    #     return num

    # start = 0
    # for end in range(k+1, len(number)):
    #     n = _max(start, end)
    #     answer += str(n[1])
    #     start = n[0]+1
    # answer += str(max(number[start:]))

    # return answer


    stack = [number[0]]
    for n in number[1:] :
        while stack and k > 0 and stack[-1] < n : 
            stack.pop()
            k -= 1
        stack.append(n)
    return ''.join(stack[:len(number)-k])




print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))