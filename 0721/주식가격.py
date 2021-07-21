def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)]
    
    for before in range(len(prices)):
        for after in range(before+1,len(prices)):
            if prices[after] < prices[before]:
                answer[before] = after-before
                break
    
    return answer


print(solution([1,2,3,2,3,1]))  #[5,4,1,2,1,0]