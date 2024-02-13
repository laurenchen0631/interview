impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        for word in words {
            if Solution::is_palindrome(&word) {
                return word;
            }
        }
        String::new()
    }

    fn is_palindrome(s: &str) -> bool {
        let s = s.as_bytes();
        let (mut i, mut j) = (0, s.len() - 1);
        while i < j {
            if s[i] != s[j] {
                return false;
            }
            i += 1;
            j -= 1;
        }
        true
    }
}