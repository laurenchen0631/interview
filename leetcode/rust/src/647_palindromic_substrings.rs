impl Solution {
    // Given a string s, return the number of palindromic substrings in it.
    pub fn count_substrings(s: String) -> i32 {
        let n = s.len();
        let s = s.as_bytes();
        let mut dp = vec![vec![false; n]; n];
        for i in 0..n {
            dp[i][i] = true;
            for j in 0..i {
                if s[i] == s[j] && (i - j < 2 || dp[j + 1][i - 1]) {
                    dp[j][i] = true;
                }
            }
        }
        let mut res = 0;
        for i in 0..n {
            for j in 0..n {
                if dp[i][j] {
                    res += 1;
                }
            }
        }
        res
    }
}