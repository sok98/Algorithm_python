import operator 

def solution(genres, plays):
    count = {}
    for i in range(len(genres)):
        if genres[i] in count:
            count[genres[i]] += plays[i]
        else:
            count[genres[i]] = plays[i]
        
    s_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    for g in s_count :
       print(g[0]) 

    
    
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))