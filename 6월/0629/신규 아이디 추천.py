def solution(new_id):
    answer = ''

    # 1단계 : 모든 대문자 소문자로 치환
    new_id = new_id.lower()

    # 2단계 : 소문자, 숫자, 가능 문자 제외 제거 후 answer에 저장
    sp = ["-", "_", "."]
    for i in new_id:
        if i.isalnum() or i in sp:
            answer += i

    # 3단계 : .가 두번 이상 나올 때 . 하나로 치환
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4단계 : 처음이나 끝에 . 위치하면 제거
    if answer and answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]

    # 5단계 : 빈 문자열이면 a 대입
    if answer == "":
        return "aaa"

    # 6단계 : 16자 이상이면 16자부터 삭제, 마지막 문자 .이면 삭제
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7단계 : 2자 이하라면 마지막 문자 3자 될때까지 반복
    elif len(answer) <= 2:
        answer += answer[-1]*(3-len(answer))

    return answer
