import collections
def twoSum(nums : [int], target : int) -> [int]:
    # check = 0
    # for i in range(len(nums)):
    #     check = target - nums[i]
    #     if check in nums[i+1:]:
    #         return  i, nums[i+1:].index(check) + (i+1)

    checkDic = collections.defaultdict()
    for i in range(len(nums)):
        checkDic[nums[i]] = i

    for i in range(len(nums)):
        if target - nums[i] in checkDic and i != checkDic[target - nums[i]]:
            return i, checkDic[target - nums[i]]


    return []


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,2,3], 6))

# (0, 1)
# (1, 2)
# (0, 2)