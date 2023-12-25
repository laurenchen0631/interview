impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let n = s.len();
        let s = s.as_bytes();
        let mut dp = vec![0; n + 1];
        dp[0] = 1;
        for i in 1..=n {
            if s[i - 1] != b'0' {
                dp[i] += dp[i - 1];
            }
            if i > 1 && s[i - 2] != b'0' && (s[i - 2] - b'0') * 10 + s[i - 1] - b'0' <= 26 {
                dp[i] += dp[i - 2];
            }
        }
        dp[n]
    }
}