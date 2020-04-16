/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */

object Solution {
    def minDepth(root: TreeNode): Int = {
        def solve(node: TreeNode, depth: Int): Int = {
            if (node == null) return Int.MaxValue
            if (node.left == null && node.right == null) return depth + 1
            return math.min(solve(node.left, depth + 1), solve(node.right, depth + 1))
        }
        if (root == null) 0 else solve(root, 0)
    }
}
