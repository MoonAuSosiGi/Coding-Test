shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    for menu in menus:
        if menu in orders:
            return True
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)