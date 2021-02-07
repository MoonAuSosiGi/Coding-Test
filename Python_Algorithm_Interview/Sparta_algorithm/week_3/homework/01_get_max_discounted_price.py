shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    result = 0
    while len(prices) > 0 and len(coupons) > 0:
        price = prices.pop(0)
        coupon = coupons.pop(0)
        result += (price - int(price * (coupon * 0.01)))

    while len(prices):
        result += prices.pop(0)
    return result


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.