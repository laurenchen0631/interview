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
    pub fn add_one_row(root: Option<Rc<RefCell<TreeNode>>>, val: i32, depth: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if depth == 1 {
            let mut new_root = TreeNode::new(val);
            new_root.left = root;
            return Some(Rc::new(RefCell::new(new_root)));
        }
        let mut root = root;
        let mut depth = depth;
        let mut stack = vec![(root.as_ref().unwrap().clone(), 1)];
        while !stack.is_empty() {
            let (node, d) = stack.pop().unwrap();
            if d == depth - 1 {
                let mut left = node.borrow_mut().left.take();
                let mut right = node.borrow_mut().right.take();
                let mut new_left = TreeNode::new(val);
                let mut new_right = TreeNode::new(val);
                new_left.left = left;
                new_right.right = right;
                node.borrow_mut().left = Some(Rc::new(RefCell::new(new_left)));
                node.borrow_mut().right = Some(Rc::new(RefCell::new(new_right)));
            } else {
                if let Some(left) = node.borrow().left.as_ref() {
                    stack.push((left.clone(), d + 1));
                }
                if let Some(right) = node.borrow().right.as_ref() {
                    stack.push((right.clone(), d + 1));
                }
            }
        }
        root
    }
}
