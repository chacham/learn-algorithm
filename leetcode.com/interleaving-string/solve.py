class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # l1, l2, l3 = len(s1), len(s2), len(s3)
        # if l1 + l2 != l3:
        #     return False
        # def helper(i1, i2, i3):
        #     if i1 == l1 and i2 == l2 and i3 == l3:
        #         return True
        #     result = False
        #     if i1 < l1 and s1[i1] == s3[i3]:
        #         result |= helper(i1+1, i2, i3+1)
        #     if i2 < l2 and s2[i2] == s3[i3]:
        #         result |= helper(i1, i2+1, i3+1)
        #     return result
        # return helper(0, 0, 0)

        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        dp = [[False] * (l2+1) for _ in range(l1+1)]

        for row, col in [(row, col) for row in range(l1+1) for col in range(l2+1)]:
            if row == 0 and col == 0:
                dp[row][col] = True
            elif row == 0:
                dp[row][col] = dp[row][col-1] and s2[col-1] == s3[row + col - 1]
            elif col == 0:
                dp[row][col] = dp[row-1][col] and s1[row-1] == s3[row + col - 1]
            else:
                dp[row][col] = (dp[row][col-1] and s2[col-1] == s3[row + col - 1]) \
                            or (dp[row-1][col] and s1[row-1] == s3[row + col - 1])
        return dp[-1][-1]
