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
    pub fn pseudo_palindromic_paths (root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }

        let mut bucket = [0; 10];
        Self::dfs(&root, &mut bucket)
    }

    fn dfs(root: &Option<Rc<RefCell<TreeNode>>>, bucket: &mut [i32; 10]) -> i32 {
        if let Some(node) = root {
            let node = node.borrow();
            bucket[node.val as usize] += 1;
            let mut count = 0;
            if node.left.is_none() && node.right.is_none() {
                if Self::is_pseudo_palindrome(bucket) {
                    count += 1;
                }
            } else {
                count += Self::dfs(&node.left, bucket);
                count += Self::dfs(&node.right, bucket);
            }
            bucket[node.val as usize] -= 1;
            return count;
        }
        0
    }

    fn is_pseudo_palindrome(bucket: &[i32; 10]) -> bool {
        let mut odd_count = 0;
        for i in 0..10 {
            if bucket[i] % 2 == 1 {
                odd_count += 1;
            }
        }
        odd_count <= 1
    }
}