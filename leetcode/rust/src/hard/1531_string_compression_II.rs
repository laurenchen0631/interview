use std::collections::HashMap;

impl Solution {
    pub fn get_length_of_optimal_compression(s: String, k: i32) -> i32 {
        let mut compression = Compression::new();
        compression.get_length_of_optimal_compression(s, k)
    }
}

struct Compression {
    cache: HashMap<(usize, usize, u8, usize), i32>,
}

impl Compression {
    fn new() -> Self {
        Self {
            cache: HashMap::new(),
        }
    }

    fn get_length_of_optimal_compression(&mut self, s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        let k = k as usize;
        self.dfs(s, 0, k, 0, 0)
    }

    fn dfs(&mut self, s: &[u8], i: usize, k: usize, last: u8, cnt: usize) -> i32 {
        if let Some(&res) = self.cache.get(&(i, k, last, cnt)) {
            return res;
        }
        
        if i == s.len() {
            return 0;
        }



        let delete = if k > 0 {
            self.dfs(s, i + 1, k - 1, last, cnt)
        } else {
            1000
        };
        let keep = if s[i] == last {
            let d = if cnt == 1 || cnt == 9 || cnt == 99 {
                1
            } else {
                0
            };
            self.dfs(s, i + 1, k, last, cnt + 1) + d
        } else {
            self.dfs(s, i+1, k, s[i], 1) + 1
        };

        self.cache.insert((i, k, last, cnt), delete.min(keep));
        delete.min(keep)
    }
}