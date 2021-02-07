from collections import deque

c = 11
b = 2


# Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.
#
# 조건은 다음과 같다.
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고,
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
#
# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다

# cony  t0  t1     t2       t3
# time  0    1      2       3
#       C   C + 1  C + 3    C +6 ...
#
# brown  B-1 or B+1 or 2*B

# cony 11
# brown 2
# cony      11           12
# brown     2-1 = 1      1-1 = 0, 1+1 = 2, 1*2 = 2
#           2+1 = 3      3-1 = 2, 3+1 = 4, 3*2 = 6
#           2*2 = 4      4-1 = 3, 4+1 = 5, 4*2 = 8
#

def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    # 위치, 시간목록
    visited = [{} for _ in range(200001)]

    while cony_loc <= 200000:
        cony_loc += time
        # 셋 중 하나를 선택해야 함
        # 연산 결과를 기억해야함 -> 시간 : 현위치
        print(cony_loc)
        if time in visited[cony_loc]:
            return time
        for i in range(0, len(queue)):
            current_pos, current_time = queue.popleft()
            new_time = current_time + 1

            brown_new_pos = current_pos - 1
            if 0 <= brown_new_pos <= 200000 and new_time not in visited[brown_new_pos]:
                visited[brown_new_pos][new_time] = True
                queue.append((brown_new_pos, new_time))

            brown_new_pos = current_pos + 1
            if 0 <= brown_new_pos <= 200000 and new_time not in visited[brown_new_pos]:
                visited[brown_new_pos][new_time] = True
                queue.append((brown_new_pos, new_time))

            brown_new_pos = current_pos * 2
            if 0 <= brown_new_pos <= 200000 and new_time not in visited[brown_new_pos]:
                visited[brown_new_pos][new_time] = True
                queue.append((brown_new_pos, new_time))
        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!
