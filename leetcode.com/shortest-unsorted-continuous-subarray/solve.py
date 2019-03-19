class Solution:
    def findUnsortedSubarray(self, nums: 'List[int]') -> 'int':
        start, end = 0, 0
        iterator = enumerate(sorted(nums))
        
        for i, n in iterator:
            if n != nums[i]:
                start = i
                break
                
        for i, n in iterator:
            if n != nums[i]:
                end = i + 1
        
        return end - start
