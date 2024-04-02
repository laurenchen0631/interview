use std::collections::HashMap;

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut map = HashMap::new();
        let mut map2 = HashMap::new();
        let mut s = s.chars();
        let mut t = t.chars();
        while let (Some(a), Some(b)) = (s.next(), t.next()) {
            if let Some(&c) = map.get(&a) {
                if c != b {
                    return false;
                }
            } else {
                map.insert(a, b);
            }
            if let Some(&c) = map2.get(&b) {
                if c != a {
                    return false;
                }
            } else {
                map2.insert(b, a);
            }
        }
        true
    }
}
