if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        s = [[int(x) for x in input().split()], [int(x) for x in input().split()]]

        if N == 1:
            print(max(s[0][0], s[1][0]))
        else:
            #print(s[0][0], s[1][0], s[0][0], s[1][0], sep='\t')
            #print(s[0][1], s[1][1], s[1][0] + s[0][1], s[0][0] + s[1][1], sep='\t')
            dp = [[0, s[0][0], s[1][0] + s[0][1]], [0, s[1][0], s[0][0] + s[1][1]]]
            #print(dp[0])
            #print(dp[1])
            for i in range(2, N):
                dp[0][0], dp[0][1] = dp[0][1], dp[0][2]
                dp[1][0], dp[1][1] = dp[1][1], dp[1][2]
                dp[0][2] = max(dp[1][0], dp[1][1]) + s[0][i]
                dp[1][2] = max(dp[0][0], dp[0][1]) + s[1][i]
                #print(s[0][i], s[1][i], dp[0][2], dp[1][2], sep='\t')
            print(max(dp[0][1], dp[0][2], dp[1][1], dp[1][2]))