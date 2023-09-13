impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let mut left = vec![1; ratings.len()];
        let mut right = vec![1; ratings.len()];

        for i in 1..ratings.len() {
            if ratings[i] > ratings[i - 1] {
                left[i] = left[i - 1] + 1;
            }
        }

        for i in (0..ratings.len() - 1).rev() {
            if ratings[i] > ratings[i + 1] {
                right[i] = right[i + 1] + 1;
            }
        }

        let mut res = 0;
        for i in 0..ratings.len() {
            res += left[i].max(right[i]);
        }
        res
    }
}