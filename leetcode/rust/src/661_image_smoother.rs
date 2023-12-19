impl Solution {
    pub fn image_smoother(img: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = img.len();
        let n = img[0].len();
        let mut res = vec![vec![0; n]; m];

        for i in 0..m {
            for j in 0..n {
                let mut sum = 0;
                let mut count = 0;

                for x in -1..=1 {
                    for y in -1..=1 {
                        let ii = i as i32 + x;
                        let jj = j as i32 + y;

                        if ii >= 0 && ii < m as i32 && jj >= 0 && jj < n as i32 {
                            sum += img[ii as usize][jj as usize];
                            count += 1;
                        }
                    }
                }

                res[i][j] = sum / count;
            }
        }
        res
    }
}