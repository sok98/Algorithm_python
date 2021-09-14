def solution(id_list, report, k):
    user = {name:idx for idx, name in enumerate(id_list)}
    reported = [set() for _ in id_list]
    answer = [0] * len(id_list)

    for r in report:
        a, b = r.split()
        reported[user[b]].add(user[a])
    
    for re in reported:
        if len(re) >= k:
            for r in re:
                answer[r] += 1
    
    return answer