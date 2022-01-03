lotto = [0, 0, 0, 0, 0, 0]
win_numbers = [31, 10, 45, 1, 6, 19]


def solution(lottos, win_nums):
    answer = []
    result1 = []
    result2 = []

    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == 0:
                result1.append(0)
                break
            if lottos[i] == win_nums[j]:
                result1.append(lottos[i])
                result2.append(lottos[i])
                continue

    result(answer, result1)
    result(answer, result2)

    return answer


def result(answer, result1):
    if len(result1) == 0:
        answer.append(6)
    elif len(result1) == 1:
        answer.append(6)
    elif len(result1) == 2:
        answer.append(5)
    elif len(result1) == 3:
        answer.append(4)
    elif len(result1) == 4:
        answer.append(3)
    elif len(result1) == 5:
        answer.append(2)
    elif len(result1) == 6:
        answer.append(1)


print(solution(lotto, win_numbers))
