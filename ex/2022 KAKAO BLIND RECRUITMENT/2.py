def solution(n, k):
    if k != 10: n = convert(n, k)
    check = list(map(int, ' '.join(str(n).split('0')).split()))
    
    max_num = max(check)
    number = [True for _ in range(max_num+1)]
    number[1] = False
    for i in range(2, int(max_num**0.5)+1):
        if number[i]:
            for j in range(2*i, max_num+1, i):
                number[j] = False
                
    answer = 0
    for a in check:
        if number[a]:
            answer += 1
    
    return answer

def convert(num, n):
    result = []
    while num != 0:
        num, a = divmod(num, n)
        result.insert(0, a)
    return ''.join(map(str, result))