# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        headK = head
        for i in range(k-1):
            headK = headK.next
        tailK = head
        last = headK.next
        while last:
            tailK = tailK.next
            last = last.next
        headK.val, tailK.val = tailK.val, headK.val
        return head
