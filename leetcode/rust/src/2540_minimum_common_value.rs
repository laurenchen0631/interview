use std::collections::HashSet;

impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let set1 = nums1.into_iter().collect::<HashSet<_>>();
        let set2 = nums2.into_iter().collect::<HashSet<_>>();

        let common = set1.intersection(&set2);
        if let Some(&val) = common.min() {
            val
        } else {
            -1
        }
    }
}