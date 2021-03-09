numbers = [1, 1, 1, 1, 1]
target_number = 3
output = []


def BT(array, target):
    if array >= len(numbers):
        output.append(target)
        return
    num = numbers[array]
    BT(array+1, target-int(num))
    BT(array+1, target+int(num))


BT(0, 0)
print(output.count(target_number))
