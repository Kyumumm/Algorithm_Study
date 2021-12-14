def first_try():
    A, B, V = map(int, input().split())

    count = 0
    total = 0
    # 처음엔 무슨 기준으로 반복문을 돌릴까 고민해봤다 -> 반복문을 돌려서 그런지 시간초과
    while 1:
        if total + A - B >= V:
            #
            break
        else:
            total = total + A - B
            count += 1

    print(count)
    return count


def second_try():
    A, B, V = map(int, input().split())
    # V = (A-B) * 일수 + A  => 마지막 A를 더해준 이유 : 마지막 날에 낮에는 A만큼 올라가서 떨어지지 않기 때문
    # 일수에 관한 식으로 바꿔주면
    # 일수 = (V-B) / (A-B)
    n = (V-B) / (A-B)
    print(int(n) if n == int(n) else int(n) + 1)
