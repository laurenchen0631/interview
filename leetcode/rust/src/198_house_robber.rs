impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut robbed = 0;
        let mut skipped = 0;

        for num in nums {
            let temp = robbed;
            robbed = skipped + num;
            skipped = skipped.max(temp);
        }

        robbed.max(skipped)
    }
}