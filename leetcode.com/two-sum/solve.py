class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        # for i, n1 in enumerate(nums):
        #     for j, n2 in enumerate(nums[i+1:], i+1):
        #         if n1 + n2 == target:
        #             return [i, j]

        m = {}
        for i, num in enumerate(nums):
            if target - num in m:
                return m[target - num], i
            m[num] = i
