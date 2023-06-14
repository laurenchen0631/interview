use std::{rc::Rc, cell::RefCell};

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


pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    let values = traverse(root);
    let mut res = values[1] - values[0];
    for i in 2..values.len() {
        res = res.min(values[i] - values[i - 1]);
    }
    res
}

pub fn traverse(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut result = vec![];
    if let Some(node) = root {
        result.append(&mut traverse(node.borrow().left.clone()));
        result.push(node.borrow().val);
        result.append(&mut traverse(node.borrow().right.clone()));
    }
    result
}