impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map = std::collections::HashMap::new();
        for s in strs {
            let mut key = s.chars().collect::<Vec<char>>();
            key.sort();
            map.entry(key).or_insert(Vec::new()).push(s);
        }

        map.into_iter().map(|(_, v)| v).collect()
    }
}