impl Solution {
    pub fn frequency_sort(s: String) -> String {
        let freq = s.chars()
            .fold(std::collections::HashMap::new(), |mut map, c| {
                *map.entry(c).or_insert(0) += 1;
                map
            });
        
        let mut chars = s.chars().collect::<Vec<char>>();
        chars.sort_unstable_by(|a, b| {
            match freq.get(b).unwrap().cmp(freq.get(a).unwrap()) {
                std::cmp::Ordering::Equal => a.cmp(b),
                other => other
            }
        });
        chars.iter().collect()
    }
}
