def solution(board, skill):
    # answer = len(board) * len(board[0])
    
    for s in skill:
        if s[0] == 1: # 적군
            for i in range(s[1], s[3]+1):
                for j in range(s[2], s[4]+1):
                    board[i][j] -= s[5]
                    # if board[i][j] <= 0 and board[i][j] > -s[5]:
                    #     answer -= 1
                    
        else :  # 아군
            for i in range(s[1], s[3]+1):
                for j in range(s[2], s[4]+1):
                    board[i][j] += s[5]
                    # if board[i][j] <= s[5]:
                    #     answer += 1
                        
        answer = 0
        for line in board:
            for x in line:
                if x > 0:
                    answer += 1
        
    return answer