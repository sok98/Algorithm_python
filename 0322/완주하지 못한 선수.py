def solution(participant, completion):
    answer = "_"
    d = {}
    for i in participant:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for c in completion:
        d[c] -= 1

    for k, v in d.items():
        if v != 0:
            answer = k

    return answer


print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]))
