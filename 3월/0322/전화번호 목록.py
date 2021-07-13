# 답 찾아보고 이해함

def solution(phone_book):
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1

    for i in phone_book:
        temp = ""
        for number in i:
            temp += number
            print("temp:", temp)
            if temp in hash_map and temp != i:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
