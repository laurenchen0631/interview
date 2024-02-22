impl Solution {
    pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
        let mut n = right;
        while n > left {
            n &= n - 1;
        }
        n
    }
}