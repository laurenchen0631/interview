impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let n = matrix.len();
        let mut dp = vec![0; n];

        for row in matrix {
            let mut tmp = vec![0; n];
            for i in 0..n {
                tmp[i] = row[i] + dp[i];
                if i > 0 {
                    tmp[i] = tmp[i].min(row[i] + dp[i - 1]);
                }
                if i + 1 < n {
                    tmp[i] = tmp[i].min(row[i] + dp[i + 1]);
                }
            }
            dp = tmp;
        }
        dp.iter().min().unwrap().clone()
    }
}