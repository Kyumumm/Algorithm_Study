shop_prices = [20000, 100000, 1500000]
user_coupons = [10, 10, 10]


def get_max_discounted_price_first(prices, coupons):
    shop_prices.sort(reverse=True)
    user_coupons.sort(reverse=True)
    total_price = 0
    index = 0

    for i in range(len(user_coupons)):
        if index >= len(shop_prices):
            return total_price
        price = int(shop_prices[i] * (100 - user_coupons[i]) / 100)
        total_price = total_price + price
        index = i + 1

    for j in range(index, len(shop_prices)):
        total_price = total_price + shop_prices[j]

    return total_price


def get_max_discounted_price(prices, coupons):
    coupons.sort(reverse=True)
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
