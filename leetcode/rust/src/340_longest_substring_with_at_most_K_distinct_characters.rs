use std::collections::HashMap;

pub fn length_of_longest_substring_k_distinct(s: String, k: i32) -> i32 {
    let mut cur_max = 0;
    let mut count: HashMap<char,i32> = HashMap::new();
    let chars = s.chars().collect::<Vec<char>>();

    for (i, c) in s.chars().enumerate() {
        count.entry(c).and_modify(|e| *e += 1).or_insert(1);
        if count.len() <= k as usize {
            cur_max += 1;
        }
        else {
            let left_char = chars[i-cur_max as usize];
            count.entry(left_char).and_modify(|e| *e -= 1);
            if count[&left_char] == 0 {
                count.remove(&left_char);
            }
        }
    }
    cur_max as i32
}