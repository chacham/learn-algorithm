class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2, k = m-1, n-1, m+n-1
        while n1 >= 0 and n2 >= 0:
            if nums1[n1] < nums2[n2]:
                nums1[k] = nums2[n2]
                n2 -= 1
                k -= 1
            else:
                nums1[k] = nums1[n1]
                n1 -= 1
                k -= 1
        while n2 >= 0:
            nums1[k] = nums2[n2]
            n2 -= 1
            k -= 1
