/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} key
 * @return {TreeNode}
 */
var deleteNode = function(root, key) {
  let parent = null;
  let removing = root;
  let leftChild = false;
  while (removing && removing.val !== key) {
    parent = removing;
    if (key < removing.val) {
      removing = removing.left;
      leftChild = true;
    } else {
      removing = removing.right;
      leftChild = false;
    }
  }

  // Not found
  if (!removing) {
    return root;
  }
  
  // No left child
  if (!removing.left) {
    if (!parent) {
      return removing.right;
    }
    if (leftChild) {
      parent.left = removing.right;
    } else {
      parent.right = removing.right;
    }
    return root;
  }

  // No right child
  if (!removing.right) {
    if (!parent) {
      return removing.left;
    }
    if (leftChild) {
      parent.left = removing.left;
    } else {
      parent.right = removing.left;
    }
    return root;
  }

  if (removing.left && !removing.left.right) {
    // Left no right child
    removing.val = removing.left.val;
    removing.left = removing.left.left;
  } else {
    // Pull left rightmost
    let rightmostParent = null;
    let rightmost = removing.left;
    while (rightmost.right) {
      rightmostParent = rightmost;
      rightmost = rightmost.right;
    }
    removing.val = rightmost.val;
    rightmostParent.right = rightmost.left;
  }
  return root;
};