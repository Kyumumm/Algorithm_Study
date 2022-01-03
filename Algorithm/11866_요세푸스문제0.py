from collections import deque
n, k = map(int, input().split())
s = deque([])
for i in range(1, n + 1):
    s.append(i)
print('<', end='')
while s:
    for i in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')

# k-1 까지 반복을 돌려서 맨 뒤로 보내 값을 살려논다 - 이게 빙글빙글 도는 것과 같다
# 그리고 반복이 끝나면 해당 값을 pop 하고 다시 반복 돌린다...
# 대단하다 !!!