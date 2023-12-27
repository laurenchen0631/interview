impl Solution {
    pub fn num_rolls_to_target(n: i32, k: i32, target: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut dp = vec![0; target as usize + 1];
        
        for i in 1..=k.min(target) as usize {
            dp[i] = 1;
        }

        for _ in 1..n as usize {
            for i in (1..=target as usize).rev() {
                dp[i] = 0;
                for j in 1..=k.min(i as i32) as usize {
                    dp[i] = (dp[i] + dp[i - j]) % MOD;
                }
            }
        }

        dp.last().unwrap().clone()
    }
}