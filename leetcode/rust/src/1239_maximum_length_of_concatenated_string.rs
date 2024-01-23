use std::collections::HashSet;

impl Solution {
    pub fn max_length(arr: Vec<String>) -> i32 {
        fn dfs(arr: &Vec<String>, s: String, start: usize) -> i32 {
            let mut chars = s.chars().collect::<HashSet<_>>();
            if chars.len() != s.len() {
                return 0;
            }

            let mut res = s.len() as i32;
            for i in start..arr.len() {
                res = res.max(
                    dfs(arr, s.clone() + arr.get(i).unwrap(), i + 1));
            }
            res
        }
        dfs(&arr, "".to_string(), 0)
    }
}