impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len() as i32;
        let n = grid[0].len() as i32;

        let mut cache = vec![vec![vec![-1; n as usize]; n as usize]; m as usize];
        fn dp(grid: &Vec<Vec<i32>>, cache: &mut Vec<Vec<Vec<i32>>>, m: i32, n: i32, r: i32, c1: i32, c2: i32) -> i32 {
            if c1 < 0 || c1 >= n || c2 < 0 || c2 >= n {
               return -1;
            }
            
            if cache[r as usize][c1 as usize][c2 as usize] != -1 {
                return cache[r as usize][c1 as usize][c2 as usize];
            }

            let mut res = grid[r as usize][c1 as usize] + if c1 != c2 { grid[r as usize][c2 as usize] } else { 0 };
            if r < m - 1 {
                let mut max = 0;
                for i in -1..=1 {
                    for j in -1..=1 {
                        max = max.max(dp(grid, cache, m, n, r + 1, c1 + i as i32, c2 + j));
                    }
                }
                res += max;
            }
            cache[r as usize][c1 as usize][c2 as usize] = res;
            res
        }
        

        dp(&grid, &mut cache, m, n, 0, 0, n - 1)
    }
}