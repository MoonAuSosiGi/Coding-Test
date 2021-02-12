from typing import List

input_nums = [1, 4, 3, 2]
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
def arrayPairSum(nums: List[int]) -> int:
    n = len(nums)
    result = 0
    nums.sort()
    pair = []
    # 1 2 3 4
    # 아래 코드를 파이썬 슬라이싱 형태로 더 간단하게
    # 2칸식 띄워서 계산
    result = sum(nums[::2])

    # 아래 코드를 좀 더 개선해서, 짝수번째만 더함 (짝수번째의 값이 작으므로)
    # for i, j in enumerate(nums):
    #     if i % 2 == 0:
    #         result += j
    # 맨 뒤의 페어와 더한 값이 젤 크다
    # for i in range(n):
    #     pair.append(nums[i])
    #     if len(pair) == 2:
    #         result += min(pair)
    #         pair = []
    # 오른차순으로 두고, 제일 큰값 위주로 찾자
    # for i in range(n-1, 0, -1):
    #     for j in range(i):
    #         pair.append(min(nums[i], nums[j]))
    #         if len(pair) == 2:
    #             sum = pair[0] + pair[1]
    #             if sum > result:
    #                 result = sum
    #             pair.clear()

    return result

print(arrayPairSum(input_nums))