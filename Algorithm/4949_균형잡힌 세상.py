# first_try
# while 1:
#     command = list(input())
#     check_bracket = []
#     check_bracket_big = []
#
#     is_empty = False
#     if "." == command[0]:
#         break
#     for i in range(len(command)):
#         if "(" in command[i]:
#             check_bracket.append(command[i])
#         if ")" in command[i]:
#             if not check_bracket:
#                 is_empty = True
#                 break
#             else:
#                 check_bracket.pop()
#
#         if "[" in command[i]:
#             check_bracket_big.append(command[i])
#         if "]" in command[i]:
#             if not check_bracket_big:
#                 is_empty = True
#                 break
#             else:
#                 check_bracket_big.pop()
#
#     if not check_bracket and not is_empty and not check_bracket_big:
#         print("yes")
#     else:
#         print("no")

# 런타임 에러
while 1:
    command = list(input())
    check_bracket = []

    is_empty = False
    if command == ".":
        break
    for i in range(len(command)):
        if "(" in command[i]:
            check_bracket.append(command[i])
        if ")" in command[i]:
            if not check_bracket and check_bracket[-1] == "[":
                is_empty = True
                break
            elif check_bracket[-1] == "(":
                check_bracket.pop()

        if "[" in command[i]:
            check_bracket.append(command[i])
        if "]" in command[i]:
            if not check_bracket and check_bracket[-1] == "(":
                is_empty = True
                break
            elif check_bracket[-1] == "[":
                check_bracket.pop()

    if not check_bracket and not is_empty:
        print("yes")
    else:
        print("no")

# 제출답안
# while True:
#     s = input()
#     if s == '.':
#         break
#     stk = []
#     temp = True
#     for i in s:
#         if i == '(' or i == '[':
#             stk.append(i)
#         elif i == ')':
#             if not stk or stk[-1] == '[':
#                 temp = False
#                 break
#             elif stk[-1] == '(':
#                 stk.pop()
#         elif i == ']':
#             if not stk or stk[-1] == '(':
#                 temp = False
#                 break
#             elif stk[-1] == '[':
#                 stk.pop()
#     if temp == True and not stk:
#         print('yes')
#     else:
#         print('no')