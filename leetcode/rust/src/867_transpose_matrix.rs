impl Solution {
    // 1  2  3 
    // 4. 5. 6

    // 1 4
    // 2 5
    // 3 6 
    pub fn transpose(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut res = vec![vec![0; m]; n];

        for i in 0..m {
            for j in 0..n {
                res[j][i] = matrix[i][j];
            }
        }
        res
    }
}