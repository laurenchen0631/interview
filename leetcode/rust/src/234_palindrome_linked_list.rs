// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}
impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut nums = Vec::new();
        let mut head = head;
        while let Some(node) = head {
            nums.push(node.val);
            head = node.next;
        }
        let mut i = 0;
        let mut j = nums.len() - 1;
        while i < j {
            if nums[i] != nums[j] {
                return false;
            }
            i += 1;
            j -= 1;
        }
        true
    }
}