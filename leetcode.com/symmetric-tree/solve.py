# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive Solution
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def _isSymmetric(left, right):
    #         if left is None and right is None:
    #             return True
    #         if left is None or right is None:
    #             return False
    #         if left.val == right.val:
    #             return _isSymmetric(left.left, right.right) and _isSymmetric(left.right, right.left)
    #         return False
    #     if root is None:
    #         return True
    #     return _isSymmetric(root.left, root.right)

    # Iterative Solution
    def isSymmetric(self, root: 'TreeNode') -> bool:
        leftStack, rightStack = [root], [root]
        while leftStack and rightStack:
            left, right = leftStack.pop(), rightStack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                leftStack.append(left.left)
                leftStack.append(left.right)
                rightStack.append(right.right)
                rightStack.append(right.left)
                continue
            return False
        return True
