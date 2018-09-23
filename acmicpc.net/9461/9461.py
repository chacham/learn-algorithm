if __name__ == "__main__":
    dp = [0,1,1,1,2,2]
    for i in range(6, 101):
        dp.append(dp[-1] + dp[-5])
    N = int(input())
    for i in range(N):
        print(dp[int(input())])
