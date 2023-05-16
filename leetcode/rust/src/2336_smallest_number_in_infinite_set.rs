use std::collections::{BinaryHeap, HashSet};
use std::cmp::Reverse;

struct SmallestInfiniteSet {
    heap: BinaryHeap<Reverse<i32>>,
    nums: HashSet<i32>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SmallestInfiniteSet {
    fn new() -> Self {
        let mut heap = BinaryHeap::new();
        let mut nums = HashSet::new();

        for i in 1..=1000 {
            heap.push(Reverse(i as i32));
            nums.insert(i as i32);
        }

        Self {
            heap,
            nums,
        }
    }
    
    fn pop_smallest(&mut self) -> i32 {
        let v: Reverse<i32> = self.heap.pop().unwrap();
        let Reverse(n) = v;
        self.nums.remove(&n);
        return n;
    }
    
    fn add_back(&mut self, num: i32) {
        if !self.nums.contains(&num) {
            self.heap.push(Reverse(num));
            self.nums.insert(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * let obj = SmallestInfiniteSet::new();
 * let ret_1: i32 = obj.pop_smallest();
 * obj.add_back(num);
 */