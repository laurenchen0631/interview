impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        let mut dp = vec![vec![vec![-1; n as usize]; m as usize]; max_move as usize + 1];
        
        fn find_path(m: i32, n: i32, max_move: i32, i: i32, j: i32, dp: &mut Vec<Vec<Vec<i32>>>) -> i32 {
            if i < 0 || i >= m || j < 0 || j >= n {
                return 1;
            }
            if max_move == 0 {
                return 0;
            }
            if dp[max_move as usize][i as usize][j as usize] != -1 {
                return dp[max_move as usize][i as usize][j as usize];
            }
            let mut res = 0;
            let MOD = 1_000_000_007;
            res = (res + find_path(m, n, max_move - 1, i - 1, j, dp)) % MOD;
            res = (res + find_path(m, n, max_move - 1, i + 1, j, dp)) % MOD;
            res = (res + find_path(m, n, max_move - 1, i, j - 1, dp)) % MOD;
            res = (res + find_path(m, n, max_move - 1, i, j + 1, dp)) % MOD;
            dp[max_move as usize][i as usize][j as usize] = res;
            res
        }

        find_path(m, n, max_move, start_row, start_column, &mut dp)
    }
}