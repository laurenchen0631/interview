use std::collections::HashSet;

impl Solution {
    // [1, 2, 2, 4]
    // [1, 2, 3, 4]
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut should_existed: HashSet<i32> = HashSet::new();
        for i in 1..=nums.len() {
            should_existed.insert(i as i32);
        }

        let mut num_set: HashSet<i32> = HashSet::new();
        for num in nums.iter() {
            num_set.insert(*num);
        }

        let set_sum = num_set.iter().sum::<i32>();
        let num_sum = nums.iter().sum::<i32>();
        let target_sum = should_existed.iter().sum::<i32>();

        return vec![num_sum - set_sum, target_sum - set_sum];
    }
}