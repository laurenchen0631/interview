impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut res = vec![vec![1]];
        for i in 1..(num_rows as usize) {
            let mut row = vec![1];
            for j in 1..i {
                row.push(res[i - 1][j - 1] + res[i - 1][j]);
            }
            row.push(1);
            res.push(row);
        }
        res
    }
}