impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut s = s.chars().collect::<Vec<char>>();
        let mut order = order.chars().collect::<Vec<char>>();
        let mut pos = vec![26; 26];
        for i in 0..order.len() {
            pos[order[i] as usize - 'a' as usize] = i;
        }

        s.sort_by(|a, b| pos[*a as usize - 'a' as usize].cmp(&pos[*b as usize - 'a' as usize]));
        s.iter().collect()
    }
}