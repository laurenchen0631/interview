impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count = 1;
        let mut candidate = nums[0];

        for n in nums[1..].iter() {
            if count == 0 {
                candidate = *n;
                count = 1;
            } else if *n == candidate {
                count += 1;
            } else {
                count -= 1;
            }
        }
        candidate
    }
}