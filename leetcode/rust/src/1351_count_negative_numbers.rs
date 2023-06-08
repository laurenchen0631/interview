pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
    grid.iter()
        .map(
            // do binary search on reversed row
            |row| (row.len() - row.partition_point(|&x| x >= 0)) as i32
        )
        .sum()
}