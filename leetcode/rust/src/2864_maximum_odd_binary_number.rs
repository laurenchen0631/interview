impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let mut s = s.chars().collect::<Vec<_>>();
        let one_count = s.iter().filter(|&&c| c == '1').count();
        let zero_count = s.len() - one_count;

        return "1".repeat(one_count-1).to_string() + &"0".repeat(zero_count) + if one_count > 0 { "1" } else { "" };
    }
}