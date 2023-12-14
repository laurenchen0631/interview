impl Solution {
    pub fn ones_minus_zeros(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut one_rows = vec![0; m];
        let mut one_cols = vec![0; n];

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    one_rows[i] += 1;
                    one_cols[j] += 1;
                }
            }
        }

        let mut res: Vec<Vec<i32>> = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                res[i][j] += one_rows[i] + one_cols[j];
                res[i][j] -= (m as i32 - one_rows[i]) + (n as i32 - one_cols[j]);
            }
        }
        res

    }
}