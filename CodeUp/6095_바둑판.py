d = [[0 for j in range(20)] for i in range(20)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split(' '))
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

#
# 1. 프로그래밍 기본 문법 공부(파이썬)
# 2. 알고리즘 기본100제(코드업:기초100제)
# 3. 백준 문제풀기(그리디, 탐색, 기초 동적프로그래밍 50문제씩)
# 4. 기출문제 풀기(프로그래머스:카카오)