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
    pub fn smallest_from_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, curr: String, res: &mut String) {
            match node {
                None => (),
                Some(node) => {
                    let n = node.borrow();
                    let mut new = ((n.val as u8 + 97) as char).to_string() + &curr;
                    if n.left.is_none() && n.right.is_none() {
                        *res = res.min(&mut new).to_string();
                        return;
                    }
                    dfs(n.left.clone(), new.clone(), res);
                    dfs(n.right.clone(), new.clone(), res);
                }
            }
        }

        let mut res = "z".to_string().repeat(400);
        dfs(root, "".to_string(), &mut res);
        res
    }
}
