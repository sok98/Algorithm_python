def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    for p in people:
        answer += 1
        if p + people[-1] <= limit:
            people.pop()
    return answer


print(solution([70, 80, 50], 100))
