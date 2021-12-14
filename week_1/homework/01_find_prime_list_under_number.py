input = 20


# 소수 찾기
def find_prime_list_under_number(number):
    i = 2
    j = 0
    number_list = [0] * number

    for index in number_list:
        number_list[j] = j + 1
        j = j + 1

    prime_array = []
    for prime in number_list:
        if prime % i == 0:
            continue
        else:
            prime_array.append(prime)

    return prime_array


def another_method(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = another_method(input)
print(result)
