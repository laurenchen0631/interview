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
    pub fn leaf_similar(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::dfs(root1) == Self::dfs(root2)
    }

    fn dfs(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res = vec![];
        if let Some(node) = root {
            if node.borrow().left.is_none() && node.borrow().right.is_none() {
                res.push(node.borrow().val);
            } else {
                res.append(&mut Self::dfs(node.borrow().left.clone()));
                res.append(&mut Self::dfs(node.borrow().right.clone()));
            }
        }
        res
    }
}