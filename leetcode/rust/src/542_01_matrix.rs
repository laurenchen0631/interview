use std::collections::{VecDeque, HashSet};

impl Solution {
    pub fn update_matrix(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut matrix = mat.clone();
        let m = mat.len();
        let n = mat[0].len();
        let mut queue: VecDeque<(i32,i32,i32)> = VecDeque::new();
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 0 {
                    queue.push_back((i as i32, j as i32, 0));
                    visited.insert((i as i32, j as i32));
                }
            }
        }

        while !queue.is_empty() {
            let (i, j, d) = queue.pop_front().unwrap();
            matrix[i as usize][j as usize] = d;
            for (x, y) in vec![(i-1, j), (i+1, j), (i, j-1), (i, j+1)] {
                if x >= 0 && x < m as i32 && 
                    y >= 0 && y < n as i32 && 
                    !visited.contains(&(x, y)) {
                    queue.push_back((x, y, d+1));
                    visited.insert((x, y));
                }
            }
        }

        matrix
    }
}