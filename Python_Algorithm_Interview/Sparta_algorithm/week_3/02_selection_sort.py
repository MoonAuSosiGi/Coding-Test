input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    # for i in range(n):
    #     select = i
    #     for j in range(i+1,n):
    #         print(j)
    #         if array[select] > array[j]:
    #             select = j
    #     array[i], array[select] = array[select], array[i]

    for i in range(n-1):
        select = i
        for j in range(n-i):
            if array[select] > array[i+j]:
                select = i + j
        array[i], array[select] = array[select], array[i]
        print(array)
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!