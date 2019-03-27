# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        if n == 0:
            return []
        def helper(l, r):
            if l == r:
                return [None]
            result = []
            for i in range(l, r):
                for left, right in [(left, right) for left in helper(l, i) for right in helper(i+1, r)]:
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    result.append(node)
            return result
        return helper(1, n+1)