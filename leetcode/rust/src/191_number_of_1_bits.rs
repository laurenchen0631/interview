impl Solution {
    pub fn hammingWeight (n: u32) -> i32 {
        let mut res = 0;
        let mut n = n;
        while n != 0 {
            res += n & 1;
            n >>= 1;
        }
        res as i32
    }
}