impl Solution {
    // You are given an integer array nums and a positive integer k.
    // Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let max = *nums.iter().max().unwrap();
        let mut res = 0;
        let mut start = 0;
        let mut maxElement = 0;

        for i in 0..nums.len() {
            if nums[i] == max {
                maxElement += 1;
            }

            while maxElement >= k {
                if nums[start] == max {
                    maxElement -= 1;
                }
                start += 1;
            }
            res += start;
        }
        res as i64
    }
}