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
    pub fn find_bottom_left_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut queue = std::collections::VecDeque::new();
        queue.push_back(root.unwrap());
        let mut result = 0;
        while !queue.is_empty() {
            let mut size = queue.len();
            for i in 0..size {
                let node = queue.pop_front().unwrap();
                if i == 0 {
                    result = node.borrow().val;
                }
                if node.borrow().left.is_some() {
                    queue.push_back(node.borrow().left.clone().unwrap());
                }
                if node.borrow().right.is_some() {
                    queue.push_back(node.borrow().right.clone().unwrap());
                }
            }
        }
        result
    }
}