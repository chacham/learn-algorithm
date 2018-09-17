dp = [(1, 0), (0, 1)]
for i in range(2, 41):
    dp.append((dp[-1][0] + dp[-2][0], dp[-1][1] + dp[-2][1]))

if __name__ == "__main__":
    for t in range(int(input())):
        print(*dp[int(input())])