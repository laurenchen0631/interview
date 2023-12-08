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
    pub fn tree2str(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        Solution::preorder(root)
    }

    fn preorder(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        if let Some(node) = root {
            let node = node.borrow();
            let mut s = String::new();
            s.push_str(&node.val.to_string());
            if node.left.is_some() || node.right.is_some() {
                s.push('(');
                s.push_str(&Self::preorder(node.left.clone()));
                s.push(')');
            }
            if node.right.is_some() {
                s.push('(');
                s.push_str(&Self::preorder(node.right.clone()));
                s.push(')');
            }
            s
        } else {
            String::new()
        }
    }
}
