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
    pub fn reverse_between(head: Option<Box<ListNode>>, left: i32, right: i32) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode {
            val: 0,
            next: head,
        }));
        let mut before = &mut dummy;
        for _ in 1..left {
            before = &mut before.as_mut()?.next;
        }
        
        let mut prev = before.as_mut()?.next.take();
        let mut cur = prev.as_mut()?.next.take();
        for _ in left..right {
            let tmp = cur.as_mut()?.next.take();
            cur.as_mut()?.next = prev;
            prev = cur;
            cur = tmp;
        }


        // before.next is taken (None)
        let mut rev_tail = &mut prev;
        for _ in left..right {
            rev_tail = &mut rev_tail.as_mut()?.next;
        }
        rev_tail.as_mut()?.next = cur;
        before.as_mut()?.next = prev;
        
        dummy.unwrap().next
        
    }
}