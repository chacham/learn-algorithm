def solve(N, S, A):
    mseDp = [[-1] * (N+1) for _ in range(N+1)]
    def mse(start, end):
        if mseDp[start][end] != -1:
            return mseDp[start][end]
        arr = A[start:end]
        mean = round(sum(arr)/len(arr))
        mse = sum(map(lambda x: (x-mean)**2, arr))
        mseDp[start][end] = mse
        return mse

    dp = [[-1] * (N+1) for _ in range(S+1)]
    def rec(s, a):
        if dp[s][a] != -1:
            return dp[s][a]
        if a == 0:
            return 0
        if s == 0:
            return 1234567890
        if s == 1:
            dp[s][a] = mse(0, a)
            return dp[s][a]
        res = 1234567890
        for i in range(a):
            res = min(res, rec(s-1, i) + mse(i, a))
        dp[s][a] = res
        return res

    return rec(S, len(A))

if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N, S = map(int, input().split())
        A = sorted([int(a) for a in input().split()])
        print(solve(N, S, A))
