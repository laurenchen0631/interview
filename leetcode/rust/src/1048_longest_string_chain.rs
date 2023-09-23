use std::collections::HashMap;

impl Solution {
    pub fn longest_str_chain(words: Vec<String>) -> i32 {
        let mut words = words;
        words.sort_by_key(|w| w.len());

        let mut dp: HashMap<&String, i32> = HashMap::new();

        for word in words.iter() {
            dp.insert(&word, 1);
            for i in 0..word.len() {
                let prev_word = format!("{}{}", &word[..i], &word[i+1..]);
                if let Some(val) = dp.get(&prev_word) {
                    dp.insert(&word, std::cmp::max(dp[word], val + 1));
                }
            }
        }

        return *dp.values().max().unwrap();
    }
}