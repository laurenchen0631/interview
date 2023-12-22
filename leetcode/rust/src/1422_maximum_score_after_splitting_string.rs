impl Solution {
    pub fn max_score(s: String) -> i32 {
        let mut left = 0;
        let mut right = s.chars().filter(|&c| c == '1').count();
        let mut res = 0;

        for c in s.chars().take(s.len() - 1) {
            if c == '0' {
                left += 1;
            } else {
                right -= 1;
            }
            res = res.max((left + right) as i32);
        }
        res
    }
}