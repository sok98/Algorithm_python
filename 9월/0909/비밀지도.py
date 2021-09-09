def solution(n, arr1, arr2):
    answer = []

    def binary(num):
        result = []
        while num != 0:
            a = num // 2
            b = num % 2
            result.insert(0, b)
            num = a

        result = ''.join(map(str, result))
        result = '0'*(n-len(result)) + result
        return result


    for i in range(n):
        arr1[i] = str(binary(arr1[i]))
        arr2[i] = str(binary(arr2[i]))

        line = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)

    return answer




print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))