#문제 개떡같이 설명 이루어짐

n = int(input())
stack = []
plus_minus = []
max_value = 0
count = 1
temp = True
for i in range(n):
    num = int(input())
    if num > max_value:
        max_value = num

    while count <= num:
        stack.append(count)
        plus_minus.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        plus_minus.append('-')
    else:
        temp = False

if not temp:
    print('NO')
else:
    for i in plus_minus:
        print(i)



