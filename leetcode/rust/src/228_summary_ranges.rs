pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
    let mut ranges: Vec<String> = vec![];
    if nums.is_empty() {
        return ranges;
    }

    let mut l = nums[0];
    let mut r = nums[0];
    for i in 1..nums.len() {
        if nums[i] == r + 1 {
            r = nums[i];
        } else {
            if l == r {
                ranges.push(l.to_string());
            } else {
                ranges.push(format!("{}->{}", l, r));
            }
            l = nums[i];
            r = nums[i];
        }
    }

    if l == r {
        ranges.push(l.to_string());
    } else {
        ranges.push(format!("{}->{}", l, r));
    }


    ranges
}