impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        if word1.len() != word2.len() {
            return false;
        }

        let mut w1_bucket = vec![0; 26];
        let mut w2_bucket = vec![0; 26];
        
        for c in word1.bytes() {
            w1_bucket[(c - b'a') as usize] += 1;
        }
        for c in word2.bytes() {
            w2_bucket[(c - b'a') as usize] += 1;
        }

        for i in 0..26 {
            if (w1_bucket[i] == 0) != (w2_bucket[i] == 0) {
                return false;
            }
        }

        w1_bucket.sort_unstable();
        w2_bucket.sort_unstable();
        w1_bucket == w2_bucket
    }
}