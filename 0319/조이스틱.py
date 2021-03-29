def solution(name):
    name = list(name)
    answer = 0
    i = 0

    while 1:
        left = 1
        right = 1
        # 알파벳 바꾸기
        if name[i] != 'A':
            answer += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        name[i] = 'A'

        # 위치 바꾸기
        if name == ['A']*len(name):
            break
        else:
            for k in range(1, len(name)):
                if name[i + k] == "A":
                    right += 1
                else:
                    break
                if name[i - k] == "A":
                    left += 1
                else:
                    break

            if right > left:
                answer += left
                i -= left
            else:
                answer += right
                i += right

    return answer
