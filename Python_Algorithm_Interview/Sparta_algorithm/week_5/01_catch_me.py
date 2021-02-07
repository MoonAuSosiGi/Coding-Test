from collections import deque

c = 11
b = 2
# 처음 위치 C에서 1초 후 1만큼 움직임.
# 이후는 가속이 붙어 매 초마다 이전 이동거리 + 1만큼 움직임
# 0초     1초 (C+1)      2초(C+3)         3초 (C+6)         4초 (C+10)       5초 (C+15)
#  C     C + 1          C +1 (+2)      C (3) + (3)      C (6) + (4)       C (10) + (5)
# 브라운은 현재 위치 B에서 다음 순간 B-1 / B+1 / 2 * B 중 하나로 움직임
# 코니와 브라운의 위치 p 는 조건 0 <= x <= 200,000
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝
# 모든 경우의수
# BFS
# 잡았다 == 같은 시간에 같은 위치에 존재해야함
# 시간은 변화함
# 위치는 코니, 브라운이 자유자재로 바뀜
# 규칙적으로 증가 -> 배열, 자유자재로 -> 딕셔너리
# 각 시간마다 브라운이 갈 수 있는 위치를 저장하고 싶다.
def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0
    queue = deque()
    # 위치와 시간을 동시에 넣음
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]
    # visited[0] = { 갔던곳 저장 2: True }
    # visited[1] = { 1:True, 3:True, 4:True } ....
    # visited[위치][시간] visited[3][5] -> 3 위치에 5초에 간적이 있는가?

    while cony_loc <= 200000:
        cony_loc += time # 시간만큼  +1
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()
            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position,new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position,new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position,new_time))

        time += 1
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!