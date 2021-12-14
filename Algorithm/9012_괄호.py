n = int(input())
for _ in range(n):
    checklist = list(input())
    stack = list()
    is_empty = False
    for i in range(len(checklist)):
        if checklist[i] == "(":
            stack.append(checklist[i])
        else:
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()

    if not stack and not is_empty:
        print("YES")
    else:
        print("NO")
