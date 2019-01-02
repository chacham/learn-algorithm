if __name__ == "__main__":
    N = int(input())
    P = [int(p) for p in input().split()]
    M = int(input())

    dp0 = [0] * N
    dp1 = [0] * N
    dp2 = [0] * N

    sum_now = sum(P[:M])
    dp0[M-1] = sum_now
    for i in range(M, N):
        sum_now -= P[i - M]
        sum_now += P[i]
        dp0[i] = max(dp0[i-1], sum_now)

    sum_now = sum(P[M:M*2])
    dp1[M*2-1] = dp0[M-1] + sum_now
    for i in range(M * 2, N):
        sum_now -= P[i - M]
        sum_now += P[i]
        dp1[i] = max(dp1[i-1], dp0[i - M] + sum_now)

    sum_now = sum(P[M*2:M*3])
    dp2[M*3-1] = dp1[2*M-1] + sum_now
    for i in range(M * 3, N):
        sum_now -= P[i - M]
        sum_now += P[i]
        dp2[i] = max(dp2[i-1], dp1[i - M] + sum_now)

    print(dp2[-1])
    # print(P)
    # print(dp0)
    # print(dp1)
    # print(dp2)
    
