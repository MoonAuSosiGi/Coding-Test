import sys
input_nums = [7, 1, 5, 3, 6, 4]


# def getMaxProfit(buy_index, prices):
#     max_profit = prices[buy_index + 1] - prices[buy_index]
#     for i in range(buy_index + 2, len(prices)):
#         profit = prices[i] - prices[buy_index]
#         if profit > max_profit:
#             max_profit = profit
#     return max_profit


def maxProfit(prices):
    max_profit = -sys.maxsize
    min_profit = sys.maxsize

    for price in prices:
        min_profit = min(min_profit, price)
        max_profit = max(max_profit, price - min_profit)
    if len(prices) == 0:
        return 0
    else:
        return max_profit
    # max_profit = getMaxProfit(0, prices)
    # for i in range(1, len(prices)-1):
    #     profit = getMaxProfit(i, prices)
    #     if profit > max_profit:
    #         max_profit = profit
    # return max_profit


print(maxProfit(input_nums))
