impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let mut left = (1 + n) * n / 2;
        let mut right = 0;
        let mut pivot = n;

        while left >= right {
            right += pivot;
            if left == right {
                return pivot;
            }
            left -= pivot;
            pivot -= 1;
        }
        return -1;
    }
}