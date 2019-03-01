class Solution:
    def productExceptSelf(self, nums):
        res = [1 for _ in nums]

        tmp = 1
        for i in range(1, len(nums)):
            tmp *= nums[i-1]
            res[i] *= tmp

        tmp = 1
        for i in reversed(range(len(nums) - 1)):
            tmp *= nums[i+1]
            res[i] *= tmp

        return res
