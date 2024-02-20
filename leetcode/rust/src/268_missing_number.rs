impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let target = (1..nums.len() as i32 + 1).into_iter().sum::<i32>();
        let sum = nums.into_iter().sum::<i32>();
        target - sum
    }
}