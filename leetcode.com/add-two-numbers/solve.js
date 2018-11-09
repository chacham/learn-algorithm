/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  function solve(l1, l2, carry) {
    let val;
    if (l1) {
      if (l2) {
        return {
          val: (l1.val + l2.val + carry) % 10,
          next: solve(l1.next, l2.next, parseInt((l1.val + l2.val + carry) / 10)),
        };
      } else {
        return {
          val: (l1.val + carry) % 10,
          next: solve(l1.next, null, parseInt((l1.val + carry) / 10)),
        };
      }
    } else if (l2){
      return {
        val: (l2.val + carry) % 10,
        next: solve(l2.next, null, parseInt((l2.val + carry) / 10)),
      };
    } else if (carry) {
      return {
        val: carry % 10,
        next: null,
      };
    } else {
      return null;
    }
  }
  
  return solve(l1, l2, 0);
};