impl Solution {
    pub fn total_money(n: i32) -> i32 {
        let m = n / 7;
        let k = n % 7;
        let prev_weeks = 28 * m + 7 * m * (m - 1) / 2;
        let last_week = k * (k + 1) / 2 + m * k;
        return prev_weeks + last_week;
    }
}