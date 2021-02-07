import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30
#
# Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다. 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고, 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies), 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때, 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.

# stock = 4
# dates = [4, 10, 15]
# supplies = [20, 5, 10]
# k = 30
# 다음과 같이 입력값이 들어온다면,
# 현재 재고가 4개 있습니다. 그리고 정상적으로 돌아오는 날은 30일까지입니다.
# 즉, 26개의 공급량을 사와야 합니다!
# 그러면 제일 최소한으로 26개를 가져오려면? supplies 에서 20, 10 을 가져오면 되겠죠?
# 그래서 이 경우의 최소 공급 횟수는 2 입니다!


# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.
# 최대한 많은 양의 라면을 가져오면 된다 x
# stock 2 고 dates[ 1 , 10] , supplies [ 10 , 100] k 11
# 재고가 바닥나는 시점 이전까지 받을 수 있는 라면 중 제일 많은 라면을 받아야 함
# 제일 많은 -> 정렬? x 라면의 재고가 동적으로 변경됨 , 2 제일 많은 값만 가져가면 됨 (?)
# 데이터를 넣을 때마다 최솟/최댓값을 동적으로 변경시키고 최솟/최댓값을 바로 꺼낼 수 있는 자료구조가 필요하다

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    heap = []
    result = 0
    cur = 0
    #[20, 5, 10]
    visits = []
    while stock < k:
        print("---- stock ",stock)
        for i in range(cur,len(dates)):
            print("dates ",dates[i], " date stock ", supplies[i], " stock ", stock)
            if dates[i] <= stock:
                heapq.heappush(heap,-supplies[i])
            else:
                cur = i
                print("cur " ,cur)
                break
            print("heap ",heap)
        result += 1
        data = -heapq.heappop(heap)
        stock += data
        visits.append(data)
    print("visits ",visits)
    return result


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))