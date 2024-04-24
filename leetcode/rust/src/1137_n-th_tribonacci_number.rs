impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let mut dp = [0, 1, 1];
        if n < 3 {
            return dp[n as usize];
        }

        for i in 3..=n {
            let tmp = dp[0] + dp[1] + dp[2];
            dp[0] = dp[1];
            dp[1] = dp[2];
            dp[2] = tmp;
        }
        dp[2]

    }
}
