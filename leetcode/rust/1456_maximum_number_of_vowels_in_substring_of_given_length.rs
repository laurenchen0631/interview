use std::collections::HashSet;

impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let mut res = 0i32;
        let voewls = HashSet::from(['a', 'e', 'i', 'o', 'u']);
        let chars = s.chars();

        for i in 0..k {
            if voewls.contains(&chars.nth(i as usize).unwrap()) {
                res += 1;
            }
        }
    }
}