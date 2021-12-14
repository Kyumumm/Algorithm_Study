N, M = map(int, input().split())
number = 5 * 10 ** (len(str(M)) - 1)
count = 0


while True:
    if M == 0:
        break
    elif M > number:
        count += 1
        M = M - number
    else:
        head = M // (10 ** (len(str(M)) - 1))
        M = M - head * (10 ** (len(str(M)) - 1))
        number = int(number / 10)
        count += head

print(count)



# 다른 정답

# n, k = map(int, input().split())
# m = []
# num = 0
# for i in range(n):
#     m.append(int(input()))
# for i in range(n - 1, -1, -1):
#     if k == 0:
#         break
#     if m[i] > k:
#         continue
#     num += k // m[i]
#     k %= m[i]
# print(num)