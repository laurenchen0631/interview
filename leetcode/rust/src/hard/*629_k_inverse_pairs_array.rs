impl Solution {
    // [1,2,3,4]
    // [1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,2,3], [1,4,3,2]
    pub fn k_inverse_pairs(n: i32, k: i32) -> i32 {
        let mut dp = vec![vec![0; k as usize + 1]; n as usize + 1];
        dp[0][0] = 1;

        for i in 1..=n as usize {
            for j in 0..=k as usize {
                dp[i][j] = if j > 0 {
                    (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
                } else {
                    dp[i - 1][j]
                };
                if j >= i {
                    dp[i][j] = (dp[i][j] + 1000000007 - dp[i - 1][j - i]) % 1000000007;
                }
            }
        }
        dp[n as usize][k as usize]
    }
}

