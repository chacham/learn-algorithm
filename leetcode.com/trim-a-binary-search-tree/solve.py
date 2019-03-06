# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: 'TreeNode', L: int, R: int) -> 'TreeNode':
        if not root:
            return root
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

#         def trimLeft(root, L):
#             if not root:
#                 return root
#             if root.val < L:
#                 return trimLeft(root.right, L)
#             root.left = trimLeft(root.left, L)
#             return root
#         def trimRight(root, R):
#             if not root:
#                 return root
#             if root.val > R:
#                 return trimRight(root.left, R)
#             root.right = trimRight(root.right, R)
#             return root
#         if not root:
#             return root
#         if root.val < L:
#             return self.trimBST(root.right, L, R)
#         if root.val > R:
#             return self.trimBST(root.left, L, R)
#         root.left = trimLeft(root.left, L)
#         root.right = trimRight(root.right, R)
#         return root