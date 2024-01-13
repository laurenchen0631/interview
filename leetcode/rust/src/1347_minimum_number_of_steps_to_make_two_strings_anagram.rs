impl Solution {
    // Minimum Number of Steps to Make Two Strings Anagram
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut s_bucket = vec![0; 26];
        let mut t_bucket = vec![0; 26];

        for c in s.chars() {
            s_bucket[c as usize - 'a' as usize] += 1;
        }

        for c in t.chars() {
            t_bucket[c as usize - 'a' as usize] += 1;
        }

        let mut res = 0;
        for i in 0..26 {
            if s_bucket[i] > t_bucket[i] {
                res += s_bucket[i] - t_bucket[i];
            }
        }
        res
    }
}