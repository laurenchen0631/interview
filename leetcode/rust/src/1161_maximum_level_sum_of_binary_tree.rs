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

pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    let mut l = 1;
    let mut res = (l, root.as_ref().unwrap().borrow().val);
    let mut q = vec![root.unwrap()];

    while !q.is_empty() {
        let mut sum = 0;
        let mut nq = vec![];
        for n in q {
            sum += n.borrow().val;
            if let Some(l) = &n.borrow().left {
                nq.push(l.clone());
            }
            if let Some(r) = &n.borrow().right {
                nq.push(r.clone());
            }
        }
        if sum > res.1 {
            res = (l, sum);
        }
        l += 1;
        q = nq;
    }
    res.0
}