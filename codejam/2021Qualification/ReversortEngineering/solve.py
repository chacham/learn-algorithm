def solve(N, C):
    already = [[False] * (C+1) for _ in range(N+1)]
    dp = [[0] * (C+1) for _ in range(N+1)]

    def rec(n, c):
        if n == 1:
            if c == 0:
                return True, [1]
            return False, []
        if n < 1 or c < 1:
            return False, []
        if already[n][c]:
            return dp[n][c]

        found, res = rec(n-1, c-1)
        if found:
            already[n][c] = True
            dp[n][c] = True, [1] + [x+1 for x in res]
            return dp[n][c]

        found, res = rec(n-1, c-n)
        if found:
            already[n][c] = True
            dp[n][c] = True, list(reversed([x+1 for x in res])) + [1]
            return True, list(reversed([x+1 for x in res])) + [1]

        already[n][c] = True
        dp[n][c] = False, []
        return dp[n][c]

    return rec(N, C)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, C = map(int, input().split())
        found, res = solve(N, C)
        if found:
            print(f"Case #{t+1}: {' '.join(map(str, res))}")
        else:
            print(f"Case #{t+1}: IMPOSSIBLE")
