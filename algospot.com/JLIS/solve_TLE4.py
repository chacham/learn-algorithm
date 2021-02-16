INF = float('inf')

if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N, M = map(int, input().split())
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]

        lisA = [1] * N
        for i in range(1, N):
            maxBefore = 0
            for j in range(i):
                if A[j] < A[i]:
                    maxBefore = max(maxBefore, lisA[j])
            lisA[i] = maxBefore

        lisB = [1] * M
        for i in range(1, M):
            maxBefore = 0
            for j in range(i):
                if B[j] < B[i]:
                    maxBefore = max(maxBefore, lisB[j])
            lisB[i] = maxBefore

        res = -1

        # dp = {(-1, -1): 0}
        dp = [[0] * (M+1) for _ in range(N+1)]
        # dpMax = {(-1, -1): -INF}
        dpMax = [[-INF] * (M+1) for _ in range(N+1)]
        for i, lis in enumerate(lisA):
            dp[i][-1] = lis
        for i, lis in enumerate(lisB):
            dp[-1][i] = lis
        for R in range(-1, N):
            for C in range(-1, M):
                maxLisBefore = -1

                for r in range(-1, R):
                    if dp[r][C] > maxLisBefore:
                        if (R >= 0 and A[R] > dpMax[r][C]) or (C >= 0 and B[C] > dpMax[r][C]):
                            maxLisBefore = dp[r][C]
                for c in range(-1, C):
                    if dp[R][c] > maxLisBefore:
                        if (R >= 0 and A[R] > dpMax[R][c]) or (C >= 0 and B[C] > dpMax[R][c]):
                            maxLisBefore = dp[R][c]

                dp[R][C] = maxLisBefore + 1
                dp[R][C] = -INF
                if R >= 0:
                    dp[R][C] = max(dp[R][C], A[R])
                if C >= 0:
                    dp[R][C] = max(dp[R][C], B[C])

        print(max(map(max, dp)))
