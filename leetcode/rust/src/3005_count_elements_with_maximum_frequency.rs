use std::collections::HashMap;

impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut max_freq = 1;
        let mut freq = HashMap::new();
        for &num in &nums {
            *freq.entry(num).or_insert(0) += 1;
            if freq[&num] > max_freq {
                max_freq = freq[&num];
                res = freq[&num];
            } else if freq[&num] == max_freq {
                res += freq[&num];
            }
            
        }
        res
    }
}