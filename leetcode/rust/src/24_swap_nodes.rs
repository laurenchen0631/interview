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

/// Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes 
pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut dummy = Some(Box::new(ListNode::new(0)));
    dummy.as_mut()?.next = head;
    let mut pointer = &mut dummy;

    while pointer.as_ref()?.next.is_some() && pointer.as_ref()?.next.as_ref()?.next.is_some() {
        let mut first = pointer.as_mut()?.next.take();
        let mut second = first.as_mut()?.next.take();
        first.as_mut()?.next = second.as_mut()?.next.take();
        second.as_mut()?.next = first;
        pointer.as_mut()?.next = second;
        pointer = &mut pointer.as_mut()?.next.as_mut()?.next;
    }

    dummy?.next
}