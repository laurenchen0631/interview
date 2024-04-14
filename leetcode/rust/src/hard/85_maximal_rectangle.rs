impl Solution {
    // [
    //     ["1","0","1","0","0"],
    //     ["1","0","1","1","1"], 
    //     ["1","1","1","1","1"],
    //     ["1","0","0","1","0"]
    // ]
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() {
            return 0;
        }
        let m = matrix.len();
        let n = matrix[0].len();
        
        let mut left = vec![0; n];
        let mut right = vec![n; n];
        let mut height = vec![0; n];

        // row 0: [0, 0, 2, 0, 0] [1, 5, 3, 5, 5] [1, 0, 1, 0, 0]
        // row 1: [0, 0, 2, 2, 2] [1, 5, 3, 5, 5] [2, 0, 2, 1, 1]
        // row 2: [0, 0, 2, 2, 2] [1, 5, 3, 5, 5] [3, 1, 3, 2, 2]
        // row 3: [0, 0, 0, 3, 0] [1, 5, 5, 4, 5] [4, 0, 0, 3, 0]
        let mut max_area = 0;

        for i in 0..m {
            let mut cur_left = 0;
            let mut cur_right = n;
            for j in 0..n {
                if matrix[i][j] == '1' {
                    height[j] += 1;
                } else {
                    height[j] = 0;
                }
            }
            for j in 0..n {
                if matrix[i][j] == '1' {
                    left[j] = left[j].max(cur_left);
                } else {
                    left[j] = 0;
                    cur_left = j + 1;
                }
            }
            for j in (0..n).rev() {
                if matrix[i][j] == '1' {
                    right[j] = right[j].min(cur_right);
                } else {
                    right[j] = n;
                    cur_right = j;
                }
            }

            println!("row {:?}: {:?} {:?} {:?}", i, left, right, height);
            for j in 0..n {
                max_area = max_area.max((right[j] - left[j]) * height[j]);
            }
        }
        max_area as i32
    }
}
