impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        let s = s.chars().collect::<Vec<_>>();
        let t = t.chars().collect::<Vec<_>>();

        let mut processed_s = vec![];
        for c in s {
            if c == '#' {
                processed_s.pop();
            } else {
                processed_s.push(c);
            }
        }
        
        let mut processed_t = vec![];
        for c in t {
            if c == '#' {
                processed_t.pop();
            } else {
                processed_t.push(c);
            }
        }

        processed_s == processed_t
    }
}