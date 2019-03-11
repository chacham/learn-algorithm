class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        # jumps = [float('inf') for _ in nums]
        # jumps[0] = 0
        # last = len(nums) - 1
        # for i, num in enumerate(nums):
        #     j = min(num, last - i)
        #     nextJump = jumps[i] + 1
        #     while j > 0 and jumps[i + j] > nextJump:
        #         jumps[i + j] = nextJump
        #         j -= 1
        # return jumps[-1]

        farthest = 0
        last_farthest = 0
        res = 0
        nums.pop() # Don't need last num
        for i, num in enumerate(nums):
            farthest = max(farthest, i + num)
            if i == last_farthest:
                res += 1
                last_farthest = farthest
        return res
