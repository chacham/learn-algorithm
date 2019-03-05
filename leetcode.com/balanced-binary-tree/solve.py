# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isBalanced(self, root: 'TreeNode') -> 'bool':
    #     def _height(_root):
    #         if _root is None:
    #             return 0
    #         return max(_height(_root.left), _height(_root.right)) + 1
    #     def _isBalanced(_root):
    #         if _root is None:
    #             return True
    #         return _isBalanced(_root.left) and _isBalanced(_root.right) \
    #             and -1 <= (_height(_root.left) - _height(_root.right))  <= 1
    #     return _isBalanced(root)
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        def _rec(_root):
            if _root is None:
                return (True, 0)
            leftBalance, leftHeight = _rec(_root.left)
            rightBalance, rightHeight = _rec(_root.right)
            return (leftBalance and rightBalance and -1 <= (leftHeight - rightHeight) <= 1,\
                    max(leftHeight, rightHeight) + 1)
        return _rec(root)[0]
