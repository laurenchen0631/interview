impl Solution {
    pub fn remove_kdigits(num: String, k: i32) -> String {
        let mut k = k as usize;
        let mut stack = Vec::new();
        for c in num.chars() {
            while k > 0 && !stack.is_empty() && stack[stack.len() - 1] > c {
                stack.pop();
                k -= 1;
            }
            stack.push(c);
        }
        while k > 0 {
            stack.pop();
            k -= 1;
        }
        let mut res = stack.into_iter().collect::<String>().trim_start_matches('0').to_string();
        if res.is_empty() {
            res = "0".to_string();
        }
        res
    }
}
