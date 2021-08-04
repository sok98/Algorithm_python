def solution(priorities, location):
    answer = 1
    target = priorities[location]
    priorities[location] = -1   # 같은 우선순위와 구별 위해 -1로 변경

    while max(priorities) > target: # target보다 큰 우선순위가 있을 때
        answer += 1
        pop = priorities.index(max(priorities))
        priorities = priorities[pop+1:] + priorities[:pop]  # i번째 값 제외 재배치
    
    return answer + priorities[:priorities.index(-1)].count(target) # 앞의 같은 우선순위 count


print(solution([2,1,9,1,9,1], 1))
