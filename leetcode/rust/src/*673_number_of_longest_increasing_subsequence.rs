pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
    let n = nums.len();
    let mut dp = vec![1; n];
    let mut count = vec![1; n];
    let mut max_len = 1;

    for i in 1..n {
        for j in 0..i {
            if nums[j] >= nums[i] {
                continue;
            }

            if dp[j] + 1 > dp[i] {
                dp[i] = dp[j] + 1;
                count[i] = count[j];
            } else if dp[j] + 1 == dp[i] {
                count[i] += count[j];
            }
            max_len = max_len.max(dp[i]);
        }
    }

    let mut res = 0;
    for i in 0..n {
        if dp[i] == max_len {
            res += count[i];
        }
    }
    res

}