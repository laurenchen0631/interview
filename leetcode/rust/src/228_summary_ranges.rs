pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
    let mut ranges: Vec<String> = vec![];
    if nums.is_empty() {
        return ranges;
    }

    let mut i = 0;
    while i < nums.len() {
        let mut j: usize = i;
        while j < nums.len() - 1 && nums[j] + 1 == nums[j + 1] {
            j += 1;
        }
        if i == j {
            ranges.push(nums[i].to_string());
        } else {
            ranges.push(format!("{}->{}", nums[i], nums[j]));
        }
        i = j + 1;
    }
    ranges
}