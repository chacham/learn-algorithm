class Solution:
    def maxArea(self, height):
        res = -1
        left, right = 0, len(height) - 1
        while left < right:
            res = max((right - left) * min(height[left], height[right]), res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res