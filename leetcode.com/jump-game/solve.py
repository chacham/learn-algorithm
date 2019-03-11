class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        maxFromHere = nums[0]
        for num in nums:
            if maxFromHere < 0:
                return False
            maxFromHere = max(num - 1, maxFromHere - 1)
        return True
