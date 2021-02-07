from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
] # -> True

# game_map = [
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", "R", "#", ".", ".", ".", "#", "#", "B", "#"],
#     ["#", ".", ".", ".", "#", ".", "#", "#", ".", "#"],
#     ["#", "#", "#", "#", "#", ".", "#", "#", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
#     ["#", ".", "#", "#", "#", "#", "#", "#", ".", "#"],
#     ["#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
#     ["#", ".", "#", ".", "#", ".", "#", ".", ".", "#"],
#     ["#", ".", ".", ".", "#", ".", "O", "#", ".", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
# ]  # -> False 를 반환해야 한다


def isWall(game_map, row, col):
    return game_map[row][col] == "#"


def move(game_map, red_row, red_col, blue_row, blue_col, hole_row, hole_col, turn):
    if turn >= 10 or game_map[blue_row][blue_col] == "O" or (red_row == blue_row and red_col == blue_col):
        return False

    if game_map[red_row][red_col] == "O":
        return True

    red_offset = blue_offset = 1
    if isWall(game_map, red_row + red_offset, red_col):     red_offset = 0
    if isWall(game_map, blue_row + blue_offset, blue_col):  blue_offset = 0

    # ->
    if move(game_map, red_row + red_offset, red_col, blue_row + blue_offset, blue_col, hole_row, hole_col, turn + 1):
        return True

    red_offset = blue_offset = -1
    if isWall(game_map, red_row + red_offset, red_col):     red_offset = 0
    if isWall(game_map, blue_row + blue_offset, blue_col):  blue_offset = 0

    if move(game_map, red_row + red_offset, red_col, blue_row + blue_offset, blue_col, hole_row, hole_col, turn + 1):
        return True

    red_offset = blue_offset = 1
    if isWall(game_map, red_row, red_col + red_offset):     red_offset = 0
    if isWall(game_map, blue_row, blue_col + blue_offset):  blue_offset = 0

    if move(game_map, red_row, red_col + red_offset, blue_row, blue_col + blue_offset, hole_row, hole_col, turn + 1):
        return True

    red_offset = blue_offset = -1
    if isWall(game_map, red_row, red_col + red_offset):     red_offset = 0
    if isWall(game_map, blue_row, blue_col + blue_offset):  blue_offset = 0

    if move(game_map, red_row, red_col + red_offset, blue_row, blue_col + blue_offset, hole_row, hole_col, turn + 1):
        return True
    return False

def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!

    turn = 1
    r_c, r_r = 1, 1
    b_c, b_r = 1, 1
    h_r, h_c = 1, 1

    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] == "R":
                r_r = i
                r_c = j
                game_map[i][j] = ""
            elif game_map[i][j] == "B":
                b_r = i
                b_c = j
                game_map[i][j] = ""
            elif game_map[i][j] == "O":
                h_r = i
                h_c = j

    print(game_map[r_r][r_c], " ", game_map[b_r][b_c])

    return move(game_map, r_r, r_c, b_r, b_c, h_r, h_c, 1)


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
