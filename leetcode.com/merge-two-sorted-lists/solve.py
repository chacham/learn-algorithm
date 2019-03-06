# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            res = l1
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next
        now = res

        while l1 and l2:
            if l1.val < l2.val:
                now.next = l1
                now = now.next
                l1 = l1.next
            else:
                now.next = l2
                now = now.next
                l2 = l2.next
        if l1:
            now.next = l1
        else:
            now.next = l2

        return res