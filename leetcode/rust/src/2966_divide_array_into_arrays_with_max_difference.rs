impl Solution {
    pub fn divide_array(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
         let mut nums = nums;
         nums.sort_unstable();
 
         let mut result = vec![vec![nums[0]]];
         for n in &nums[1..] {
             let last = result.last_mut().unwrap();
             let start = last[0];
 
             if *n - start <= k && last.len() < 3 {
                 last.push(*n);
             } else {
                if last.len() < 3 {
                    return vec![];
                }
                result.push(vec![*n]);
             }
         }
 
         if result.last().unwrap().len() < 3 {
             return vec![];
         }
         return result;
     }
 
}