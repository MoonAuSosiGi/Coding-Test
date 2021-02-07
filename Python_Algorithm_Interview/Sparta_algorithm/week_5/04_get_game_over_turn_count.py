k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def get_position(pos, dir):
    return [pos[0] + dr[dir], pos[1] + dy[dir]]

def get_inverse_dir(dir):
    if dir == 0:
        return 1
    elif dir == 1:
        return 0
    elif dir == 2:
        return 3
    elif dir == 3:
        return 2
    return -1

def get_map_color(pos, game_map):
    if pos[0] < 0 or pos[0] >= len(game_map) or pos[1] < 0 or pos[1] >= len(game_map[0]):
        return -1
    else:
        return game_map[pos[0]][pos[1]]

def move_horse(horse, game_map):
    # horse [x,y,방향]
    # 0 오른쪽 1 왼쪽 2 위쪽 3 아래쪽
    new_pos = get_position([horse[0], horse[1]], horse[2])
    color = get_map_color(new_pos, game_map)
    if color == -1:
        # 반대 방향으로
        horse[2] = get_inverse_dir(horse[2])
        return False
    # 흰색 , 빨간색
    elif color == 0 or color == 1:
        horse[0], horse[1], horse[2] = new_pos[0], new_pos[1], horse[2]
        return True
    # 파란색
    elif color == 2:
        dir = get_inverse_dir(horse[2])
        new_pos = get_position([horse[0], horse[1]], dir)
        # 또 파란색인 경우엔 이동하지 않고 방향만 바꿈

        if get_map_color(new_pos, game_map) == 2:
            horse[2] = dir
            return True

        horse[0], horse[1], horse[2] = new_pos[0], new_pos[1], dir
        return True




# 종료 조건
# 1. 말이 4개 이상 쌓일 경우
# 2. 게임이 종료되는 턴이 1,000보다 크거나 종료되지 않을 경우 -1 반환
#
# 흰색칸 : 평범하게 이동. 가려는 곳에 말이 있다면 그 위에 쌓인다.
# 빨간색 : 이동 후에 이동한 말과 그 위의 말의 순서를 뒤집는다.
# 파란색 : 이동방향을 반대로 하고 한칸 이동 (바꾼 후 이동하려는 칸이 파란색이거나, 못가는 곳이면 가만히 있는다.)
def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    turn = 0
    # index, x, y , 방향
    horse_stack = {i: [] for i in range(len(horse_location_and_directions))}

    test_pos = [0,1,0]
    result = move_horse(test_pos,game_map)

    if result:
        # 만약 이동한 곳에 다른 노드가 있다면,
        # 흰색인 경우 그 위에 말이 올라감
        # 빨간색인 경우엔 뒤집고 그 위에 올린다
        # [index, row, col, dir]
        print("이동완료")

    print(test_pos, " map color ", get_map_color(test_pos, game_map), " ",get_map_color([0,2],game_map))
    horse_list = []
    while turn < 1000:
        for i in range(horse_location_and_directions):
            result = move_horse(horse_location_and_directions[i], game_map)

            if result:
                horse = horse_location_and_directions[i]
                color = get_map_color(horse, game_map)
                # 이 위치에 누가 있는가?
                # 기존에 있는 친구 위에 뭐가 올라가있다면?
                for j in range(horse_location_and_directions):
                    if i == j:
                        continue
                    another_horse = horse_location_and_directions[j]
                    if another_horse[0] == horse[0] and another_horse[1] == horse[1]:
                        print("test....")
                if color == 0:
                    print("흰색")
                elif color == 1:
                    print ("빨간색")
        turn += 1
    return


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
