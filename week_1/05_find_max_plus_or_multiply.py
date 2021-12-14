input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    max_value = 0
    for value in array:
        if value <= 1 or max_value <= 1:
            max_value = max_value + value
        else:
            max_value = max_value * value

    return max_value


result = find_max_plus_or_multiply(input)
print(result)
