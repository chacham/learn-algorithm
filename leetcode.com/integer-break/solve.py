class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            maxRes = -1
            for j in range(1, i):
                maxRes = max(maxRes, max(j, dp[j]) * max(i-j, dp[i-j]))
            dp[i] = maxRes
        return dp[-1]
