shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    count = 0

    for i in range(len(menus)):
        for j in range(len(orders)):
            if menus[i] == orders[j]:
                count += 1

    if count == len(orders):
        return True
    else:
        return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)