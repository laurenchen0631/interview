use std::{cmp::Reverse, collections::BinaryHeap};

impl Solution {
    pub fn furthest_building(heights: Vec<i32>, bricks: i32, ladders: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        let mut bricks = bricks;
        let mut res = 0;
        for i in 1..heights.len() {
            let diff = heights[i] - heights[i - 1];
            if diff <= 0 {
                continue;
            }
            heap.push(Reverse(diff));
            if heap.len() as i32 > ladders {
                bricks -= heap.pop().unwrap().0;
            }
            if bricks < 0 {
                return (i - 1) as i32;
            }
        }
        heights.len() as i32 - 1
    }
}