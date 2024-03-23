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
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        let len = Self::length(&head);

        let mut ptr = head.as_mut();
        for _ in 0..(len / 2) {
            if let Some(node) = ptr {
                ptr = node.next.as_mut();
            }
        }

        if let Some(node) = ptr {
            let reverse = Self::reverse(node.next.take(), None);

            if let Some(node) = head {
                node.next = Self::merge(reverse, node.next.take(), len - 1);
            }
        }
    }

    fn length(mut head: &Option<Box<ListNode>>) -> usize {
        let mut count = 0;
        while let Some(node) = head {
            head = &node.next;
            count += 1;
        }
        count
    }

    fn reverse(
        head: Option<Box<ListNode>>,
        accumulator: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        match head {
            None => accumulator,
            Some(mut node) => {
                let next = node.next;
                node.next = accumulator;

                Self::reverse(next, Some(node))
            }
        }
    }

    fn merge(
        mut left: Option<Box<ListNode>>,
        right: Option<Box<ListNode>>,
        count: usize,
    ) -> Option<Box<ListNode>> {
        if count == 0 {
            None
        } else {
            match (left.as_mut(), right.as_ref()) {
                (None, None) => None,
                (Some(_), None) => left,
                (None, Some(_)) => right,
                (Some(l), Some(_)) => {
                    l.next = Self::merge(right, l.next.take(), count - 1);
                    left
                }
            }
        }
    }
}
}