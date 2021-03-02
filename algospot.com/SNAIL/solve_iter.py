dp = [[0] * 1001 for _ in range(1001)]
for i in range(1001):
    dp[0][i] = 1
    dp[1][i] = 1
dp[1][0] = 0
dp[2][1] = 0.75
for h in range(2, 1001):
    for d in range(2, 1001):
        dp[h][d] = dp[h-2][d-1] * 0.75 + dp[h-1][d-1] * 0.25

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        N, M = map(int, input().split())
        print("{:.10f}".format(dp[N][M]))
