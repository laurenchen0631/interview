impl Solution {
    pub fn number_of_matches(n: i32) -> i32 {
        let mut res = 0;
        let mut n = n;
        while n > 1 {
            if n % 2 == 0 {
                res += n / 2;
                n /= 2;
            }
            else {
                res += (n - 1) / 2;
                n = (n - 1) / 2 + 1;
            }
        }
        res
    }
}