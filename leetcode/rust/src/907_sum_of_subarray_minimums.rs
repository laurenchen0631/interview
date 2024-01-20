impl Solution {
    // [1,2,3,4]
    // 
    pub fn sum_subarray_mins(arr: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut stack: Vec<usize> = vec![];
        let MOD = 1_000_000_007;

        for r in 0..=arr.len() {
            while !stack.is_empty() && (r == arr.len() || arr[*stack.last().unwrap()] >= arr[r]) {
                let m: i32 = stack.pop().unwrap() as i32;
                let l: i32 = if stack.is_empty() {
                    -1
                } else {
                    *stack.last().unwrap() as i32
                };
                let count: i32 = (r as i32 - m) * (m - l);
                res = (count as usize * arr[m as usize] as usize + res) % MOD;
            }
            stack.push(r);
        }

        res as i32
    }
}
