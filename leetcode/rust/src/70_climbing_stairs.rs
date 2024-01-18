impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut dp = vec![0,1,2];
        dp[1] = 1;
        dp[2] = 2;
        for i in 3..=n as usize {
            dp.push(dp[i-1] + dp[i-2])
        }
        dp[n as usize]
    }
}