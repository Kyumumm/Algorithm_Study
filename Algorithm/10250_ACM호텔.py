T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    ho = N // H
    cheng = 0
    if N % H == 0:
        cheng = H
    else:
        ho += 1
        cheng = N % H

    print(100 * cheng + ho)
