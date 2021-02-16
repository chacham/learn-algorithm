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

        dp = {(-1, -1): 0}
        dpMax = {(-1, -1): -INF}
        for i, lis in enumerate(lisA):
            dp[(i, -1)] = lis
        for i, lis in enumerate(lisB):
            dp[(-1, i)] = lis
        for R in range(-1, N):
            for C in range(-1, M):
                maxLisBefore = -1
                for r in range(-1, R+1):
                    for c in range(-1, C+1):
                        if r == R and c == C:
                            break;
                        if dp[(r, c)] > maxLisBefore:
                            if (R >= 0 and A[R] > dpMax[(r, c)]) or (C >= 0 and B[C] > dpMax[(r, c)]):
                                maxLisBefore = dp[(r, c)]

                dp[(R, C)] = maxLisBefore + 1
                dpMax[(R, C)] = -INF
                if R >= 0:
                    dpMax[(R, C)] = max(dpMax[(R, C)], A[R])
                if C >= 0:
                    dpMax[(R, C)] = max(dpMax[(R, C)], B[C])

        print(max(dp.values()))
