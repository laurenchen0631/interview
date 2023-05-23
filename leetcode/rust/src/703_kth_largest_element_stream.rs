use std::{collections::BinaryHeap, cmp::Reverse};

struct KthLargest {
    k: i32,
    heap: BinaryHeap<Reverse<i32>>,
}

impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut heap = BinaryHeap::with_capacity(k as usize);
        for num in nums {
            heap.push(Reverse(num));
            if heap.len() > k as usize {
                heap.pop();
            }
        }
        Self { k, heap }
    }
    
    fn add(&mut self, val: i32) -> i32 {
        self.heap.push(Reverse(val));
        if self.heap.len() > self.k as usize {
            self.heap.pop();
        }

        let rev = self.heap.peek().unwrap();
        let Reverse(v) = *rev;
        v
    }
}
