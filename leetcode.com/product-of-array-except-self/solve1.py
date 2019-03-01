class Solution:
    def productExceptSelf(self, nums):

        lower = [1 for _ in nums]
        for i in range(1, len(nums)):
            lower[i] = lower[i-1] * nums[i-1]

        higher = [1 for _ in nums]
        for i in reversed(range(0, len(nums) - 1)):
            higher[i] = higher[i+1] * nums[i+1]

        return [low * high for (low, high) in zip(lower, higher)]