import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_chicken_distance(house_r, house_c, chicken_r, chicken_c):
    return abs(house_r - chicken_r) + abs(house_c + chicken_c)

# 여러개 중에서 M 개를 고른 뒤, 모든 치킨 거리의 합이 가장 작게 되는 경우의 합
# -> 여러개 중에서 특정 개수를 뽑는 경우의 수
# -> 모든 치킨의 경우의 수를 다 구해야 함 -> 조합 사용

def get_min_city_chicken_distance(n, m, city_map):
    # 집마다 치킨집에 대한 거리를 다 구함
    # 치킨집을 하나씩 빼봄
    # 모든 치킨집 조합을 구함? -> 모든 조합을 돌면서 치킨거리가 제일 짧은걸 찾기?
    chicken_location_list = []
    home_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i,j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i,j])

    chicken_location_list_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_list_m_combination in chicken_location_list_m_combinations:
        city_chicken_distance = 0
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_list_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            city_chicken_distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)
    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
