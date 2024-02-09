impl Solution {
    pub fn largest_divisible_subset(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let mut dp = vec![1; n];
        let mut pre = vec![0; n];
        let mut max_index = 0;
        for i in 0..n {
            for j in 0..i {
                if nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1;
                    pre[i] = j;
                }
            }
            if dp[i] > dp[max_index] {
                max_index = i;
            }
        }
        let mut res = vec![];
        for _ in 0..dp[max_index] {
            res.push(nums[max_index]);
            max_index = pre[max_index];
        }
        res
    }
}