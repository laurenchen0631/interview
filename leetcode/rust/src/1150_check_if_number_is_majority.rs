pub fn is_majority_element(nums: Vec<i32>, target: i32) -> bool {
    if nums[0] > target || nums[nums.len() - 1] < target {
        return false;
    }

    let r = nums.partition_point(|x| *x <= target);
    let l = nums.partition_point(|x| *x < target);
    r - l > nums.len() / 2
}