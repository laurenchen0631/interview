impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        let n = mat.len();
        for i in 0..n {
            res += mat[i][i] + mat[i][n - i - 1];
        }
        if n % 2 == 1 {
            res - mat[(n / 2)][n / 2]
        } else {
            res
        }
    }
}