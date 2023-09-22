impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        if s.len() > t.len() {
            return false;
        }
        if s == "" {
            return true;
        }

        let mut s: Vec<char> = s.chars().collect();
        let mut t: Vec<char> = t.chars().collect();
        let mut i = 0;
        for c2 in t {
            let c1 = s[i];
            if c1 == c2 {
                i += 1;
            }

            if i == s.len() {
                break;
            }
        }

        false
    }
}