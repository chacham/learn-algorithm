# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        sumA = 0
        head = headA
        while head:
            sumA += head.val
            head = head.next

        sumB = 0
        head = headB
        while head:
            sumB += head.val
            head = head.next

        while headA and headB:
            if headA == headB:
                return headA
            if sumA > sumB:
                sumA -= headA.val
                headA = headA.next
            else:
                sumB -= headB.val
                headB = headB.next

        return None
