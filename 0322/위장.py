def solution(clothes):
    d = {}
    answer = 0
    for i in clothes:
        d[i[0]] = i[1]
    answer += len(d)

    return answer


print(solution([["crowmask", "face"], ["bluesunglasses", "face"],
                ["smoky_makeup", "face"]]))
