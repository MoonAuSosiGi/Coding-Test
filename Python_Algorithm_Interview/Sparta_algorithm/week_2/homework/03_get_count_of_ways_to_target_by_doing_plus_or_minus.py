numbers = [1, 1, 1, 1, 1]
target_number = 3

# 2 3 + 1 = 6       +++
# 2 3 -1 = 4        ++-    앞은 ++ (+-
# 2 -3 1 = 0
# 2 -3 -1 = -2
# -2 3 1 = 2
# -2 3 -1 = 0
# -2 -3 1 = -4
# -2 -3 -1 = 7
# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N-1의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 됨
# [2,3]
# 1 +2 +3 +1 -> +2 +3 +1
#         -1 -> +2 +3 -1
# 2 +2 -3 +1 -> +2 -3 +1
#         -1 -> +2 -3 -1
# 3 -2 +3 +1 -> -2 +3 +1
#         -1 -> -2 +3 -1
# 4 -2 -3 +1 -> -2 -3 +1
#         -1 -> -2 -3 -1

# all_ways = result = []
# current_index = 0
# current_sum = 0
# 2 3 1

def get_all_ways_to_by_doing_plus_or_minus(array, target, current_index, current_sum, success_ways):
    if current_index == len(numbers):
        if target == current_sum:
            success_ways.append(current_sum)
        return

    get_all_ways_to_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + numbers[current_index], success_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - numbers[current_index], success_ways)

#print(get_all_ways_to_by_doing_plus_or_minus(numbers,0,0,result))
#print(result)
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    success_ways = []
    get_all_ways_to_by_doing_plus_or_minus(array,target,0,0,success_ways)

    return len(success_ways)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!