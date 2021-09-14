def solution(places):
    answer = []
    for room in places:
        check = 1
        for x in range(5):
            for y in range(5):
                if room[x][y] == "P":
                    # 옆이나 아래에 응시자 있을 경우 거리두기 실패
                    if y+1 < 5 and room[x][y + 1] == "P":
                        check = 0
                        break
                    if x+1 < 5 and room[x + 1][y] == "P":
                        check = 0
                        break

                    # 대각선에 응시자가 있을 때 사이에 빈 테이블이 있는 경우 거리두기 실패
                    if x + 1 < 5 and y + 1 < 5 and room[x + 1][y + 1] == "P":
                        if room[x][y + 1] == "O" or room[x + 1][y] == "O":
                            check = 0
                            break
                    if x + 1 < 5 and y - 1 >= 0 and room[x + 1][y - 1] == "P":
                        if room[x][y - 1] == "O" or room[x + 1][y] == "O":
                            check = 0
                            break

                    # 빈 테이블을 사이에 두고 응시자가 있을 때 거리두기 실패
                    if x + 2 < 5 and room[x + 1][y] == "O" and room[x + 2][y] == "P":
                        check = 0
                        break
                    if y + 2 < 5 and room[x][y + 1] == "O" and room[x][y + 2] == "P":
                        check = 0
                        break
            if check == 0:
                break
        answer.append(check)

    return answer