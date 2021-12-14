finding_target = 5
finding_numbers = [0, 3, 5, 6, 1, 2, 4]
# [0,1,2,3,4,5,6]


def is_exist_target_number_binary(target, numbers):
    cur_min = 0
    cur_max = len(numbers) - 1
    guess = (cur_max + cur_min) // 2
    numbers.sort()
    count = 0

    while cur_min <= cur_max:
        if target == guess:
            return count
        elif guess < target:
            cur_min = guess + 1
        else:
            cur_max = guess - 1
        guess = (cur_max + cur_min) // 2
        count += 1

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
