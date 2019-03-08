# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        def nextPosition(root, num):
            if not root:
                return None, None
            parent, now = None, root
            while True:
                if not now or now.val < num:
                    return parent, now
                else: # now.val > num:
                    parent, now = now, now.right
        root = None
        for num in nums:
            parent, left = nextPosition(root, num)
            node = TreeNode(num)
            node.left = left
            if not parent:
                root = node
            else:
                parent.right = node
        return root
