top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    result = [0 for i in range(len(heights))]
    cur_tower_index = len(heights) - 1
    while cur_tower_index > 0:
        cur_check_tower_index = cur_tower_index - 1
        while cur_check_tower_index > 0:
            # print("tower ", cur_tower_index)
            # print(heights[cur_check_tower_index], " ", heights[cur_tower_index], " check " ,cur_check_tower_index)
            if heights[cur_check_tower_index] > heights[cur_tower_index]:
                result[cur_tower_index] = cur_check_tower_index+1
                break
            cur_check_tower_index -= 1

        cur_tower_index -= 1

    return result

def get_receiver_top_orders2(heights):
    result = [0] * len(heights)
    while heights:
        height = heights.pop()
        for idx in range(len(heights)-1,-1, -1):
            if heights[idx] > height:
                result[len(heights)] = idx+1
                break
    return result

print(get_receiver_top_orders2(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!