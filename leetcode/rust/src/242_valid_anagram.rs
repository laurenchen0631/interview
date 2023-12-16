use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() { return false; }

        let mut counter = HashMap::new();
        for c in s.chars() {
            let count = counter.entry(c).or_insert(0);
            *count += 1;
        }

        for c in t.chars() {
            if counter.contains_key(&c) && *counter.get(&c).unwrap() > 0 {
                let count = counter.entry(c).or_insert(0);
                *count -= 1;
            } else {
                return false;
            }
        }
        return true;
    }
}