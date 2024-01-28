use std::collections::HashMap;

impl Solution {
    pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();

        // [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        // [[0, 0, 0, 0], [0, 1, 3, 6], [0, 5, 12, 21], [0, 12, 27, 45]]
        let mut prefix_sum = vec![vec![0; n + 1]; m + 1];
        for i in 1..=m {
            for j in 1..=n {
                prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1];
            }
        }

        let mut count = 0;
        for l in 1..=m {
            for r in l..=m {
                let mut map = HashMap::new();
                map.insert(0, 1);
                for j in 1..=n {
                    let sum = prefix_sum[r][j] - prefix_sum[l - 1][j];
                    if let Some(&v) = map.get(&(sum - target)) {
                        count += v;
                    }
                    *map.entry(sum).or_insert(0) += 1;
                }
            }
        }
        count
    }
}