array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    result = []
    while len(array1) > 0 and len(array2) > 0:
        if array1[0] > array2[0]:
            result.append(array2.pop(0))
        else:
            result.append(array1.pop(0))
    if len(array1) > 0:
        result.extend(array1)
    elif len(array2) > 0:
        result.extend(array2)

    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!