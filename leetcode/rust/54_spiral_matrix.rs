impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut m = matrix.len();
        let mut n = matrix[0].len();
        let mut res = vec![0; m * n];
        let mut i = 0;
        let mut j = 0;
        let mut k = 0;
        let mut l = 0;
        let mut idx = 0;
        while i < m && j < n {
            for k in j..n {
                res[idx] = matrix[i][k];
                idx += 1;
            }
            i += 1;
            for k in i..m {
                res[idx] = matrix[k][n - 1];
                idx += 1;
            }
            n -= 1;
            if i < m {
                for k in (j..n).rev() {
                    res[idx] = matrix[m - 1][k];
                    idx += 1;
                }
                m -= 1;
            }
            if j < n {
                for k in (i..m).rev() {
                    res[idx] = matrix[k][j];
                    idx += 1;
                }
                j += 1;
            }
        }
        res
    }
}