use std::collections::VecDeque;

impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut result = vec![];
        let mut queue = VecDeque::from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
        while let Some(num) = queue.pop_front() {
            if num >= low && num <= high {
                result.push(num);
            }
            let last_digit = num % 10;
            if last_digit < 9 {
                queue.push_back(num * 10 + last_digit + 1);
            }
        }
        result
    }
}