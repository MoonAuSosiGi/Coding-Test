# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):

    stack = []
    visits = []

    stack.append(start_node)

    while len(stack) > 0: # stack: 으로 표현해도 됨
        node = stack.pop()
        visits.append(node)
        for other_node in adjacent_graph[node]:
            if other_node not in visits:
                stack.append(other_node)

    return visits


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!