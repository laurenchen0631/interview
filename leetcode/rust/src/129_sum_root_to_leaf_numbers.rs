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
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 0;
        let mut path = vec![];
        Self::dfs(&root, 0, &mut res);
        res
    }

    fn dfs(root: &Option<Rc<RefCell<TreeNode>>>, val: i32, res: &mut i32) {
        if let Some(node) = root {
            let node = node.borrow();
            let val = val * 10 + node.val;
            if node.left.is_none() && node.right.is_none() {
                *res += val;
            } else {
                Self::dfs(&node.left, val, res);
                Self::dfs(&node.right, val, res);
            }
        }
    }
}
