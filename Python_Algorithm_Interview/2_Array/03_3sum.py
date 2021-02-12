from typing import List

input_nums = [-1, 0, 1, 2, -1, -4]
#
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력
def threeSum(nums: List[int]) -> List[List[int]]:
    # 브루스 포스 2
    n = len(nums)
    result = []
    nums.sort()
    print(nums)
    for i in range(n-2):
        # 중복 체크
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, n-1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            # 정렬된 값이므로, 한칸씩 움직여본다.
            # sum이 0보다 크다면, right를 줄여본다
            if sum > 0:
                right -= 1
            # sum이 0보다 작다면, left를 늘려본다.
            elif sum < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # 중복된 값이 있을 수도 있으니까, 증감 처리
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return result

    # 브루스 포스 방식
    # n = len(nums)
    # result = []
    # nums.sort()
    # for i in range(n-2):
    #     if i > 0 and nums[i] == nums[i-1]:
    #         continue
    #     for j in range(i+1, n-1):
    #         if j > i+1 and nums[j] == nums[j-1]:
    #             continue
    #         for k in range(j+1, n):
    #             if k > j+1 and nums[k] == nums[k-1]:
    #                 continue
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 result.append([nums[i], nums[j], nums[k]])
    # return result

# [
#   [ -1, 0, 1],
#   [ -1, -1, 2]
# ]
print(threeSum(input_nums))
