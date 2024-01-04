use std::collections::HashMap;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut count = HashMap::new();
        for n in nums {
            count.entry(n).and_modify(|e| *e += 1).or_insert(1);
        }

        let mut res = 0;
        for v in count.values() {
            if *v == 1 {
                return -1;
            }
            res += (*v as f32 / 3.0).ceil() as i32;
        }
        res
    }
}
// 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
// x, 1, 1, 2, 2, 2, 3, 3, 3, 3,  4,  4,  5, 5, 5, 6