use std::collections::HashSet;

impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut nums_set = HashSet::new();
        let mut res = -1;
        for num in nums {
            nums_set.insert(num);
            if nums_set.contains(&-num) {
                res = res.max(num.abs());
            }
        }
        res
    }
}
