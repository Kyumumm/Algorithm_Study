input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array:
        if number.__eq__(num):
            return True
        else:
            return False


result = is_number_exist(8, input)
print(result)
