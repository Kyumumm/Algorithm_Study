K = int(input())

sum_money = []

for _ in range(K):
    money = int(input())

    if money == 0:
        sum_money.pop()
    else:
        sum_money.append(money)

print(sum(sum_money))