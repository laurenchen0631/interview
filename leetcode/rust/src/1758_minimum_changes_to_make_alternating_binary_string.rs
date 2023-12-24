impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let mut start0 = 0;
        // 0101
        for (i, c) in s.chars().enumerate() {
            if i % 2 == 0 && c == '1' {
                start0 += 1;
            } else if i % 2 == 1 && c == '0' {
                start0 += 1;
            }
        }
        start0.min(s.len() - start0) as i32
    }
}