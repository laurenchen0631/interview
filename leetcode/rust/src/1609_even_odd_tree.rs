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
    pub fn is_even_odd_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut q = std::collections::VecDeque::new();
        q.push_back(root);
        let mut level = 0;
        while !q.is_empty() {
            let mut prev = if level % 2 == 0 { i32::MIN } else { i32::MAX };
            let mut len = q.len();
            for _ in 0..len {
                let node = q.pop_front().unwrap().unwrap();
                let node = node.borrow();
                if level % 2 == 0 {
                    if node.val % 2 == 0 || node.val <= prev {
                        return false;
                    }
                } else {
                    if node.val % 2 == 1 || node.val >= prev {
                        return false;
                    }
                }
                prev = node.val;
                if let Some(left) = &node.left {
                    q.push_back(Some(left.clone()));
                }
                if let Some(right) = &node.right {
                    q.push_back(Some(right.clone()));
                }
            }
            level += 1;
        }
        true
    }
}