import operator 

def solution(genres, plays):
    answer = []
    count = {}
    details = {}
    for i in range(len(genres)):
        if genres[i] in count:
            count[genres[i]] += plays[i]
            details[genres[i]].append([i, plays[i]])
        else:
            count[genres[i]] = plays[i]
            details[genres[i]] = [[i, plays[i]]]

    # 정렬    
    s_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    for d in details:
        details[d] = sorted(details[d], key=lambda x:x[1], reverse=True)

    for g in s_count :
        for i in details[g[0]][:2]:
            answer.append(i[0])

    return answer
    
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))