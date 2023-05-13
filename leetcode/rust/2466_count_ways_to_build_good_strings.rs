impl Solution {
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        const MOD: i32 = 1e9 as i32 + 7;
        let mut dp = vec![0 as i32; (high+1) as usize];
        dp[0] = 1;
        for i in 1..=high {
            let i = i as usize;
            if i >= (zero as usize) {
                dp[i] = (dp[i] + dp[i-zero as usize]) % MOD;
            }
            if i >= (one as usize) {
                dp[i] = (dp[i] + dp[i-one as usize]) % MOD;
            }
            dp[i] = dp[i] % MOD;
        }

        let mut ans: i32 = 0;
        for i in low..=high {
            ans = (ans + dp[i as usize]) % MOD;
        }
        ans  
    }
}