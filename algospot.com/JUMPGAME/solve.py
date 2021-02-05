if __name__ == "__main__":
    C = int(input())
    for c in range(C):
        N = int(input())
        BOARD = [[int(x) for x in input().split()] for _ in range(N)]

        dp = [[False] * N for _ in range(N)]
        dp[0][0] = True
        for r in range(N):
            for c in range(N):
                if dp[r][c]:
                    hop = BOARD[r][c]
                    if r + hop < N:
                        dp[r + hop][c] = True
                    if c + hop < N:
                        dp[r][c + hop] = True

        if dp[-1][-1]:
            print("YES")
        else:
            print("NO")
