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
    pub fn max_ancestor_diff(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }

        let mut max_diff = 0;
        let mut stack = vec![(root.unwrap(), i32::MAX, i32::MIN)];
        while !stack.is_empty() {
            let (node, min, max) = stack.pop().unwrap();
            let node = node.borrow();
            let val = node.val;

            let new_min = min.min(val);
            let new_max = max.max(val);
            let diff = new_max - new_min;
            max_diff = max_diff.max(diff);
            if node.left.is_some() {
                stack.push((node.left.as_ref().unwrap().clone(), new_min, new_max));
            }
            if node.right.is_some() {
                stack.push((node.right.as_ref().unwrap().clone(), new_min, new_max));
            }
        }
        max_diff
    }
}