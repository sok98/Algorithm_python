def solution(price, money, count):
    
    total = 0
    for i in range(1, count+1):
        total += i
    
    return max(0, total*price - money)