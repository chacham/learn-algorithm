if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N = int(input())
        S = [int(x) for x in input().split()]
        dp = [1] * N
        for n in range(1, N):
            bfMax = 0
            for i in range(n):
                if S[i] < S[n]:
                    bfMax = max(bfMax, dp[i])
            dp[n] = bfMax + 1
        print(max(dp))
