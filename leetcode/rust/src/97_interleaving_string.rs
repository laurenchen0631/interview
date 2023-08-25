impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        let m = s1.len();
        let n = s2.len();
        let s1 = s1.chars().collect::<Vec<char>>();
        let s2 = s2.chars().collect::<Vec<char>>();
        let s3 = s3.chars().collect::<Vec<char>>();

        let mut dp = vec![vec![false; n + 1]; m + 1];

        if m + n != s3.len() {
            return false;
        }

        dp[0][0] = true;
        for j in 1..=n {
            dp[0][j] = dp[0][j - 1] && s2[j - 1] == s3[j - 1];
        }
        for i in 1..=m {
            dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
        }

        for i in 1..=m {
            for j in 1..=n {
                if dp[i-1][j] && s1[i-1] == s3[i+j-1] {
                    dp[i][j] = true;
                }
                else if dp[i][j-1] && s2[j-1] == s3[i+j-1] {
                    dp[i][j] = true;
                }
            }
        }

        return dp[m][n];
    }
}