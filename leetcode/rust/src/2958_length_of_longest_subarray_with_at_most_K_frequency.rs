use std::collections::HashMap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq = HashMap::new();
        let mut l = 0;
        let mut res = 0;

        for (r, num) in nums.iter().enumerate() {
            *freq.entry(num).or_insert(0) += 1;

            while freq[&num] > k as usize {
                let left = nums[l];
                *freq.get_mut(&left).unwrap() -= 1;
                l += 1;
            }

            res = res.max(r - l + 1);
        }
        res as i32
    }
}