struct TrieNode {
    children: Vec<Option<Box<TrieNode>>>,
    is_word: bool,
}

impl Clone for TrieNode {
    fn clone(&self) -> Self {
        Self {
            children: self.children.clone(),
            is_word: self.is_word,
        }
    }
}

impl TrieNode {
    fn new() -> Self {
        Self {
            children: vec![None; 26],
            is_word: false,
        }
    }

    fn insert(&mut self, word: &str) {
        let mut node = self;
        for c in word.chars() {
            let idx = (c as u8 - b'a') as usize;
            node = node.children[idx].get_or_insert_with(|| Box::new(TrieNode::new()));
        }
        node.is_word = true;
    }
}

impl Solution {
    pub fn index_pairs(text: String, words: Vec<String>) -> Vec<Vec<i32>> {
        let mut trie = TrieNode::new();
        for word in words {
            trie.insert(&word);
        }

        let mut res: Vec<Vec<i32>> = vec![];

        for i in 0..text.len() {
            let mut node = &trie;
            for j in i..text.len() {
                let idx = (text.as_bytes()[j] - b'a') as usize;
                if let Some(child) = &node.children[idx] {
                    node = child;
                    if node.is_word {
                        res.push(vec![i as i32, j as i32]);
                    }
                } else {
                    break;
                }
            }
        }
        return res
    }
}