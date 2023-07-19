pub fn erase_overlap_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
    intervals.sort();
    let mut res = 0;
    let mut prev = std::i32::MIN;
    for i in intervals {
        if i[0] >= prev {
            prev = i[1];
        } else {
            res += 1;
        }
    }
    res
}