impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut sorted = heights.clone();
        sorted.sort();
        heights.iter().zip(sorted.iter()).filter(|(a, b)| a != b).count() as i32
    }
}
