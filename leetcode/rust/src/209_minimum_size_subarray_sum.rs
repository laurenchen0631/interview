pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
    let mut l = 0;
    let mut res = nums.len() + 1;
    let mut cur = 0;
    for i in 0..nums.len() {
        cur += nums[i];
        while cur >= target && l <= i {
            res = res.min(i - l + 1);
            cur -= nums[l];
            l += 1;
        }
    }
    if res == nums.len() + 1 {
        return 0;
    }
    res as i32
}