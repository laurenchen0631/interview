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
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max = 0;
        Self::depth(&root, &mut max);
        max
    }

    fn depth(root: &Option<Rc<RefCell<TreeNode>>>, max: &mut i32) -> i32 {
        if let Some(node) = root {
            let node = node.borrow();
            let left = Self::depth(&node.left, max);
            let right = Self::depth(&node.right, max);
            *max = std::cmp::max(*max, left + right);
            std::cmp::max(left, right) + 1
        } else {
            0
        }
    }
}