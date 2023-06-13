use std::collections::HashMap;

pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
    let n = grid.len();
    let mut count = 0i32;

    let mut rows = HashMap::new();
    for row in &grid {
        rows.entry(row)
            .and_modify(|f| *f += 1)
            .or_insert(1);
    }

    for col in 0..n {
        let mut key = Vec::new();
        for row in 0..n {
            key.push(grid[row][col]);
        }
        count += rows.get(&key).unwrap_or(&0);
    }

    count
}
