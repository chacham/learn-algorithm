/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */
object Solution {
    def kthSmallest(root: TreeNode, k: Int): Int = {
        def solve(root: TreeNode, k: Int): Tuple2[Int, Int] = {
            if (root == null) return (k, 0)
            solve(root.left, k) match {
                case (0, res) => (0, res)
                case (1, _) => (0, root.value)
                case (left, _) => solve(root.right, left - 1)
            }
        }
        solve(root, k)._2
    }
}
