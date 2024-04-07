impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut stack = Vec::new();
        let mut s = s.chars().collect::<Vec<_>>();
        for i in 0..s.len() {
            if s[i] == '(' || s[i] == '*' {
                stack.push(i);
            } else {
                if stack.is_empty() {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        let mut stack = Vec::new();
        for i in (0..s.len()).rev() {
            if s[i] == ')' || s[i] == '*' {
                stack.push(i);
            } else {
                if stack.is_empty() {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        true
    }
}