impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut res = 0;
        let mut left = 0;
        let mut min_index = -1;
        let mut max_index = -1;
        for (right, &num) in nums.iter().enumerate() {
            if num > max_k || num < min_k {
                left = right + 1;
                min_index = -1;
                max_index = -1;
            }
            if num == min_k {
                min_index = right as i64;
            }
            if num == max_k {
                max_index = right as i64;
            }
            res += 0.max(min_index.min(max_index) - left as i64 + 1);
        }
        res as i64
    }
}