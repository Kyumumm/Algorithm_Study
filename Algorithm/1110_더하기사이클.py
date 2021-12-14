def change_number(number):
    x1 = number // 10
    y1 = number % 10

    if x1 + y1 < 10:
        z = x1 + y1
    else:
        z = (x1 + y1) % 10
    return 10 * y1 + z


N = int(input())
x = change_number(N)
count = 1
while True:
    if not x == N:
        x = change_number(x)
        count += 1
    else:
        print(count)
        break
