class Solution:
    def findPeakElement(self, nums: 'List[int]') -> 'int':
        ## First O(n)
        # if len(nums) == 1:
        #     return 0
        # if nums[0] > nums[1]:
        #     return 0
        # if nums[-1] > nums[-2]:
        #     return len(nums)-1
        # for i in range(1, len(nums) - 1):
        #     if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
        #         return i
        
        ## Second O(lg(n))
        # def _helper(start, end):
        #     if end - start == 1:
        #         return start
        #     if end - start == 2:
        #         if nums[start] > nums[end-1]:
        #             return start
        #         return end - 1
        #     # start - end >= 3
        #     mid = (start + end - 1) // 2
        #     if nums[mid - 1] > nums[mid]:
        #         return _helper(start, mid)
        #     elif nums[mid + 1] > nums[mid]:
        #         return _helper(mid+1, end)
        #     else:
        #         return mid
        # return _helper(0, len(nums))
        
        ## Third O(lg(n)) Shortened
        def _helper(l, r):
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                return _helper(l, mid)
            return _helper(mid+1, r)
        return _helper(0, len(nums)-1)
