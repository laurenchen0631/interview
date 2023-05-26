
use std::cmp;

impl Solution {
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        let mut dp = vec![vec![0; piles.len()]; piles.len()];
        let mut sum = vec![0; piles.len()];
        sum[piles.len() - 1] = piles[piles.len() - 1];
        for i in (0..piles.len() - 1).rev() {
            sum[i] = sum[i + 1] + piles[i];
        }
        return helper(&mut dp, &sum, &piles, 0, 1);
    }
}


fn helper(dp: &mut Vec<Vec<i32>>, sum: &Vec<i32>, piles: &Vec<i32>, start: usize, m: usize) -> i32 {
    if start >= piles.len() {
        return 0;
    }
    if start + 2 * m >= piles.len() {
        return sum[start];
    }

    if dp[start][m] != 0 {
        return dp[start][m];
    }

    // minmax algorithm to find the min value of the next player
    let mut min = std::i32::MAX;
    for x in 1..=2 * m {
        min = cmp::min(
            min,
            helper(dp, sum, piles, start + x, cmp::max(x, m))
        );
    }

    dp[start][m] = sum[start] - min;
    dp[start][m]
}