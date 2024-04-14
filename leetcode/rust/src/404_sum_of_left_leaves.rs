// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut sum = 0;
        if let Some(node) = root {
            let node = node.borrow();
            if let Some(left) = &node.left {
                let left = left.borrow();
                if left.left.is_none() && left.right.is_none() {
                    sum += left.val;
                }
            }
            sum += Solution::sum_of_left_leaves(node.left.clone());
            sum += Solution::sum_of_left_leaves(node.right.clone());
        }
        sum
    }
}
