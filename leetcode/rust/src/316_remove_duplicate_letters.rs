impl Solution {
    pub fn remove_duplicate_letters(s: String) -> String {
        let mut stack = vec![];
        let mut seen = vec![false; 26];
        let mut last_occurrence = vec![0; 26];
        for (i, c) in s.chars().enumerate() {
            last_occurrence[c as usize - 'a' as usize] = i;
        }

        for (i, c) in s.chars().enumerate() {
            let c = c as usize - 'a' as usize;
            if seen[c] {
                continue;
            }
            while let Some(&last) = stack.last() {
                if last > c && last_occurrence[last] > i {
                    seen[last] = false;
                    stack.pop();
                } else {
                    break;
                }
            }
            seen[c] = true;
            stack.push(c);
        }

        stack.iter().map(|&c| (c as u8 + 'a' as u8) as char).collect()
    }
}