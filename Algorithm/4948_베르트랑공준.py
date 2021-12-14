import math

result = []


def c(a, b):
    cnt = 0
    check = [True] * (b + 1)

    for i in range(2, int(math.sqrt(b) + 1)):
        if check[i] == True:
            for j in range(i * 2, b + 1, i):
                check[j] = False

    for i in range(a + 1, b + 1):  # a보다 크고 b보다 작은 수를 구하기 때문에 3<x<7 x=4,5,6 3개
        if check[i] == True:
            cnt += 1
    return cnt


while True:
    a = int(input())
    if a == 0:
        break
    result.append(c(a, 2 * a))

for i in result:
    print(i)
