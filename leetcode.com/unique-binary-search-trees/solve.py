class Solution:
    def numTrees(self, n: int) -> int:
        memo = {0:1, 1:1}
        def helper(n):
            if n in memo:
                return memo[n]
            memo[n] = 0
            for i in range(n):
                memo[n] += helper(i) * helper(n-i-1)
            return memo[n]
        return helper(n)
