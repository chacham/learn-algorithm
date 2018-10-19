if __name__ == "__main__":
    N, M = map(int, input().split())
    MAP = [[int(x) for x in input().split()] for n in range(N)]

    dp = [[MAP[0][0]]]
    for i in range(1, M):
        dp[0].append(dp[0][i-1] + MAP[0][i])

    for row in range(1, N):
        dp.append([])
        for col in range(M):
            dp[row].append(dp[row-1][col] + MAP[row][col])

        left = [n for n in dp[row]]
        for col in range(1, M):
            left[col] = max(dp[row][col], left[col-1] + MAP[row][col])

        right = [n for n in dp[row]]
        for col in range(M-2, -1, -1):
            right[col] = max(dp[row][col], right[col+1] + MAP[row][col])

        for col in range(M):
            dp[row][col] = max(dp[row][col], left[col], right[col])

    print(dp[-1][-1])
