import sys
sys.setrecursionlimit(10000)

dp = [[-1] * (1001) for _ in range(1001)]
for i in range(1001):
    dp[i][0] = 0
    dp[i][1] = 0
for i in range(1001):
    dp[0][i] = 1
    dp[1][i] = 1
dp[0][0], dp[0][1] = 1, 1
dp[1][0], dp[1][1] = 0, 1
dp[2][1] = 0.75

def solve(N, M):
    def rec(restHeight, restDays):
        if dp[restHeight][restDays] != -1:
            return dp[restHeight][restDays]
        dp[restHeight][restDays] = rec(restHeight-2, restDays-1) * 0.75 + rec(restHeight-1, restDays-1) * 0.25
        return dp[restHeight][restDays]
    return rec(N, M)

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        N, M = map(int, input().split())
        print("{:.10f}".format(solve(N,M)))
