def solve(N, K, P, S):
    dp = {}
    def rec(si, p):
        if si < 0:
            return 0
        if (si, p) in dp:
            return dp[(si, p)]

        res = rec(si-1, p)
        acc = 0
        for i in range(min(K, p)):
            acc += S[si][i]
            res = max(res, rec(si-1, p-i-1) + acc)
        dp[(si, p)] = res
        return res
    return rec(N-1, P)

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N, K, P = map(int, input().split())
        S = [[int(x) for x in input().split()] for _ in range(N)]

        print("Case #{}: {}".format(t, solve(N, K, P, S)))
