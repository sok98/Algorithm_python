from string import ascii_uppercase
alphabet = list(ascii_uppercase)
point = 0


def solution(name):
    answer = 0
    global point
    for i in range(len(name)):
        if name[i] != "A":
            if i - point < point + len(name) - i:
                answer += i - point
            else:
                answer += point + len(name) - i

            point = i

            if alphabet.index(name[i]) < 26 - alphabet.index(name[i]):
                answer += alphabet.index(name[i])
            else:
                answer += 26 - alphabet.index(name[i])

    return answer


print(solution("JEROEN"))
