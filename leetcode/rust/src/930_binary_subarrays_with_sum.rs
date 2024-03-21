use std::collections::HashMap;

impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        let mut count = 0;
        let mut sum = 0;
        let mut map = HashMap::new();
        map.insert(0, 1);
        for num in nums {
            sum += num;
            count += *map.get(&(sum - goal)).unwrap_or(&0);
            *map.entry(sum).or_insert(0) += 1;
        }
        count
    }
}