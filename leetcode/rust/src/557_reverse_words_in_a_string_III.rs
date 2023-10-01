use std::vec;

impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut res = String::new();
        let mut stack = vec![];
        for c in s.chars() {
            if c == ' ' {
                while let Some(c) = stack.pop() {
                    res.push(c);
                }
                res.push(' ');
            } else {
                stack.push(c);
            }
        }
        while let Some(c) = stack.pop() {
            res.push(c);
        }
        res
        // s.split_whitespace().rev().collect::<Vec<&str>>().rev.join(" ")
    }
}