
impl Solution {
    pub fn largest_odd_number(num: String) -> String {
        for i in (0..num.len()).rev() {
            if num[i..i+1].parse::<i32>().unwrap() % 2 == 1 {
                return num[0..i+1].to_string();
            }
        }
        return "".to_string();
    }
}