impl Solution {
    pub fn add_digits(num: i32) -> i32 {
        if num == 0 {
            return 0;
        }

        let n = num % 9;
        if n == 0 {9} else {n}
    }
}