use std::collections::HashSet;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut count = 0;
        let mut set = HashSet::new();
        for c in s.chars() {
            if set.contains(&c) {
                set.remove(&c);
                count += 2;
            } else {
                set.insert(c);
            }
        }
        if !set.is_empty() {
            count += 1;
        }
        count
    }
}
