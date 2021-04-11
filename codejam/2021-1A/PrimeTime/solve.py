def solve(M, P, N):
    total = sum([p * n for p, n in zip(P, N)])
    def dfs(mul, tot):
        if mul == tot:
            return tot
        if mul > tot:
            return 0
        res = 0
        for i in range(len(P)):
            if N[i] > 0:
                N[i] -= 1
                res = max(res, dfs(mul * P[i], tot - P[i]))
                N[i] += 1
        return res
    return dfs(1, total)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        M = int(input())
        P, N = [], []
        for m in range(M):
            p, n = map(int, input().split())
            P.append(p)
            N.append(n)

        print(f"Case #{t+1}: {solve(M, P, N)}")
