impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut res = vec![0; temperatures.len()];
        let mut stack = Vec::new(); // monotonic index stack 

        for i in 0..temperatures.len() {
            while !stack.is_empty() && temperatures[i] > temperatures[*stack.last().unwrap()] {
                let j = stack.pop().unwrap();
                res[j] = (i - j) as i32;
            }
            stack.push(i);
        }
        res
    }
}