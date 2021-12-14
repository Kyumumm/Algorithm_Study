s = ")())"


def is_correct_parenthesis(string):
    bracket = []
    for i in range(len(string)):
        if string[i] == "(":
            bracket.append(string[i])
        if string[i] == ")":
            if not bracket:
                return False
            bracket.pop()
        if string[len(string) - 1] == "(":
            return False

    if not bracket:
        return True
    return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
