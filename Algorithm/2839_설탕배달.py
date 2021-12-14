N = int(input())

# 포대를 최소화 하기 위해선 5kg 의 포대가 많을수록 좋음
count = 0
while N >= 0:
    if N % 5 == 0:
        count += (N // 5)
        print(count)
        break
    N -= 3
    count += 1
else:
    print(-1)
