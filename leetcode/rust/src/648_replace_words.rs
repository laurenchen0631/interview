use std::collections::HashSet;

impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {
        let roots = dictionary.into_iter().collect::<HashSet<_>>();
        let mut result = String::new();
        for word in sentence.split_whitespace() {
            let mut root = String::new();
            for (i, c) in word.chars().enumerate() {
                root.push(c);
                if roots.contains(&root) {
                    break;
                }
            }
            result.push_str(&root);
            result.push(' ');
        }
        result.pop();
        result
    }
}
