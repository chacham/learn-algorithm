# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root, k):
            if not root:
                return (k, 0)
            rest, result = inorder(root.left, k)
            if rest == 0:
                return (0, result)
            elif rest == 1:
                return (0, root.val)
            else:
                return inorder(root.right, rest - 1)

        return inorder(root, k)[1]
