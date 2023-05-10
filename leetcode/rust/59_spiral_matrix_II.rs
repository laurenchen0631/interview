impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        let mut mat = vec![vec![0; n as usize]; n as usize];
        let [mut top, mut bottom, mut left, mut right] = [0, (n - 1) as usize, 0, (n - 1) as usize];
        let mut num = 1;
        while top <= bottom && left <= right {
            for i in left..=right {
                mat[top][i] = num;
                num += 1;
            }
            top += 1;
            for i in top..=bottom {
                mat[i][right] = num;
                num += 1;
            }
            right -= 1;
            if top <= bottom {
                for i in (left..=right).rev() {
                    mat[bottom][i] = num;
                    num += 1;
                }
                bottom -= 1;
            }
            if left <= right {
                for i in (top..=bottom).rev() {
                    mat[i][left] = num;
                    num += 1;
                }
                left += 1;
            }
        }
        mat
    }
}