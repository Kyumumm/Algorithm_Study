n = int(input())
atm = list(map(int, input().split()))
sum_time = 0
sum_real_time = 0
array = []
atm.sort()
for i in range(len(atm)):
    sum_time = sum_time + atm[i]
    sum_real_time = sum_time
    array.append(sum_real_time)

print(sum(array))

