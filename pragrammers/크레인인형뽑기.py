board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    boom_doll = 0
    stack_doll = []
    count = 0

    for i in moves:
        index = i - 1
        for j in range(len(board)):
            if board[j][index] > 0:
                stack_doll.append(board[j][index])
                board[j][index] = 0
                if stack_doll[-1:] == stack_doll[-2:-1]:
                    count = count + 1
                    stack_doll = stack_doll[:-2]
                break

    return count * 2


print(solution(board, moves))
