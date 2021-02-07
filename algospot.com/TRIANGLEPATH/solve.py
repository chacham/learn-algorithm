if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N = int(input())
        TRIANGLE = [[int(x) for x in input().split()] for n in range(N)]
        dp = [TRIANGLE[0]]
        for n in range(1, N):
            row = []
            for c in range(n + 1):
                maxCur = -1
                if c > 0:
                    maxCur = max(maxCur, TRIANGLE[n][c] + dp[-1][c-1])
                if c < n:
                    maxCur = max(maxCur, TRIANGLE[n][c] + dp[-1][c])
                row.append(maxCur)
            dp.append(row)
        print(max(dp[-1]))
