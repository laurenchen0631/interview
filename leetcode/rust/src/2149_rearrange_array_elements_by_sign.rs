impl Solution {
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![];
        let mut pos_idx = 0;
        let mut neg_idx = 0;

        for _ in 0..nums.len() / 2 {
            while nums[pos_idx] < 0 {
                pos_idx += 1;
            }
            res.push(nums[pos_idx]);
            pos_idx += 1;

            while nums[neg_idx] >= 0 {
                neg_idx += 1;
            }
            res.push(nums[neg_idx]);
            neg_idx += 1;
        }
        res
    }
}