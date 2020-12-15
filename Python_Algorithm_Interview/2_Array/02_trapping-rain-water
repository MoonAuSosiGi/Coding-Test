def trap(height : [int]) -> int:
    if not height:
        return 0
    wallStack = []
    result = 0

    '''
    # 스택으로 계산하기 ( 스택엔 배열의 index 가 들어간다. )
    # 변곡점 ( 지금 체크하고 있는 높이가, stack의 top 보다 높다면 변곡점 )이 되었다면 스택에서 하나씩 꺼내서 계산
    # {스택 계산 로직}
    # 변곡점이 아니라면 패스
    # 스택에 값 추가

    # {스택 계산 로직}
    # 스택에 값이 있고, 현재 높이가, 스택의 top의 높이보다 크다면 스택을 순회한다.
    #   top 을 꺼냄 (pop)
    #   새로 변경된 스택의 top을 이용해 거리를 계산
    #       현재 인덱스 - 현재 스택의 top -1
    #   물이 얼마나 들어갈 수 있는지 계산
    #       최소값( 현재 벽의 높이, 현재 스택의 top의 높이 ) - 꺼낸 top의 높이
    #   거리와 물을 곱해 실제 물 계산
    #       때라서 물은 1칸씩 계산됨
    '''
    for i in range(len(height)):
        while wallStack and height[i] > height[wallStack[-1]]:
            top = wallStack.pop()
            if len(wallStack) == 0:
                break;
            # 거리 계산
            distance = i - wallStack[-1] - 1
            # 물 높이 계산
            waters = min(height[i], height[wallStack[-1]]) - height[top]
            result += waters * distance
        wallStack.append(i)

    return result

#print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9