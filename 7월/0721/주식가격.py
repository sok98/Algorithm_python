def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)]

    # 스택 사용
    
    prices_index = [0]
    for after in range(1, len(prices)):
        while prices_index:
            before = prices_index[-1]

            if prices[before] > prices[after]:  #가격이 떨어졌으면
                answer[before] = after - before
                prices_index.pop()
            
            else:
                break
        
        prices_index.append(after)
    return answer


    # 이중반복문 사용

    # for before in range(len(prices)):
    #     for after in range(before+1,len(prices)):
    #         if prices[after] < prices[before]:
    #             answer[before] = after-before
    #             break
    
    # return answer


print(solution([1,2,3,2,3,1]))  #[5,4,1,2,1,0]