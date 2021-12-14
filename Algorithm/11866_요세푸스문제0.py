N, M = map(int, input().split())
yosepus = []
sort_array = []

count = M - 1

for i in range(N):
    yosepus.append(i+1)

for _ in range(N):
    if count > M:
        count = len(yosepus) - count
        sort_array.append(yosepus[count])

    else:
        sort_array.append(yosepus[count])
        count = count + M

print(sort_array)
