from typing import List
from functools import reduce
input_nums = [1, 2, 3, 4]

# 배열을 입력 받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
# 나눗셈을 하지 않고 O(n)에 풀이하라
def productExceptSelf(nums: List[int]) -> List[int]:
    result = []
    # 왼쪽, 오른쪽을 나눠서 연산 하는 방법
    # 왼쪽 부터 1 2 3 4
    # [2 3 4]
    #  1 2 6
    #  12 4 1
    p = 1
    for i in range(len(nums)):
        result.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= p
        p *= nums[i]

    # 하나씩 뺀 리스트를 곱하는 방법
    # new_nums = []
    # for i in range(len(nums)):
    #     new_nums.append(list(nums))
    #     new_nums[i].pop(i)
    # for i in range(len(nums)):
    #     result.append(reduce(lambda x,y : x * y, new_nums[i]))
    return result
# [24, 12, 8, 6]
print(productExceptSelf(input_nums))