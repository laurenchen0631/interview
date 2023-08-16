use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut res = Vec::new();
        let mut deque = VecDeque::new();
        for i in 0..nums.len() {
            while !deque.is_empty() && nums[*deque.back().unwrap()] < nums[i] {
                deque.pop_back();
            }
            deque.push_back(i);
            if i as i32 >= k - 1 {
                res.push(nums[*deque.front().unwrap()]);
                if *deque.front().unwrap() as i32 == i as i32 - k + 1 {
                    deque.pop_front();
                }
            }
        }
        res
    }
}