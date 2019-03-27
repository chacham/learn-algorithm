# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(higher_bound, lower_bound, root):
            if root == None:
                return True

            result = True
            if root.left:
                result = result and lower_bound < root.left.val < root.val
            if root.right:
                result = result and root.val < root.right.val < higher_bound
            return result \
                and helper(root.val, lower_bound, root.left) \
                and helper(higher_bound, root.val, root.right)

        return helper(float('inf'), float('-inf'), root)
