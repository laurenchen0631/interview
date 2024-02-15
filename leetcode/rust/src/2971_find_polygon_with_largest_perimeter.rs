impl Solution {
    // [1,12,1,2,5,50,3] -> [1,2,3,5,12,50]
    pub fn largest_perimeter(nums: Vec<i32>) -> i64 {
        let mut nums = nums;
        nums.sort_unstable();

        let mut total = nums.iter().map(|&x| x as i64).sum::<i64>();
        for i in (2..nums.len()).rev() {
            let length = nums[i] as i64;
            if length < total - length {
                return total;
            }
            total -= length;
        }
        -1
    }
}