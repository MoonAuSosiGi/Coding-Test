current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
def get_back_dir(d):
    if d == 0:
        d = 2
    elif d == 1:
        d = 3
    elif d == 2:
        d = 0
    elif d == 3:
        d = 1
    return d
def get_rotate_dir(d):
    d -= 1
    if d < 0:
        d = 3
    return d
def get_node(r,c,d,room_map):
    node = [r,c]
    dir_pos_arr = [[node[0]-1, node[1]],[node[0],node[1]+1],[node[0]+1,node[1]],[node[0],node[1]-1]]
    return dir_pos_arr[d]

def get_dir_local(d):
    if d == 0:
        return "북"
    elif d == 1:
        return "동"
    elif d == 2:
        return "남"
    elif d == 3:
        return "서"

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    # r, c (북 , 서 기준)
    # d = 0 북쪽 1 동쪽 2 남쪽 3 서쪽
    #    x    y
    # 북  0  -1
    # 동  1   0
    # 남  0   1
    # 서 -1   0
    queue = [[r,c]]
    n = len(room_map)
    m = len(room_map[0])
    room_map[r][c] = 2
    clean_count = 1
    while queue:
        node = queue.pop(0)
        rotate_d = d
        # 방향별 모두 체크
        for i in range(4):
            rotate_d = get_rotate_dir(rotate_d)
            rotate_node_index = get_node(node[0],node[1],rotate_d,room_map)
            print("i ", i," cur ",node, " cur d " ,get_dir_local(d)," rotate ", get_dir_local(rotate_d), " node ",rotate_node_index, " n ",n, " m ",m)
            # 범위 내에 있는지
            if 0 <= rotate_node_index[0] < n and 0 <= rotate_node_index[1] < m:
                rotate_node = room_map[rotate_node_index[0]][rotate_node_index[1]]
                # 청소할 수 있는지
                if rotate_node == 0:
                    # 방향 전환, 청소
                    d = rotate_d
                    room_map[rotate_node_index[0]][rotate_node_index[1]] = 2
                    queue.append(rotate_node_index)
                    clean_count += 1
                    print("청소 ! ",queue)
                    break

            # 네 방향 모두 청소할 수 없을 경우를 찾음
            if i == 3:
                # 뒤에도 벽인지 체크해야함
                back_d = get_back_dir(d)
                back_node_index = get_node(node[0],node[1],back_d,room_map)
                print("--> back ! i ", i," cur ",node, " cur d " ,get_dir_local(d)," back ", get_dir_local(back_d), " node ",back_node_index, " n ",n, " m ",m)
                if 0 <= back_node_index[0] < n and 0 <= back_node_index[1] < m:
                    back_node = room_map[back_node_index[0]][back_node_index[1]]
                    queue.append(back_node_index)
                    if back_node == 1:
                        return clean_count

    print("!! ", clean_count)
    return room_map
# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))