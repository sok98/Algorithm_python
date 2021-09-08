def solution(board, moves):
    answer = 0
    basket = []

    for m in moves:
        for b in board:
            if b[m-1] != 0:
                if basket and basket[-1] == b[m-1]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(b[m-1])
                b[m-1] = 0
                break

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
 [1,5,3,5,1,2,1,4]))