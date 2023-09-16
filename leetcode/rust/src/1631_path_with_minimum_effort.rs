use std::{collections::{HashSet, BinaryHeap}, cmp::Reverse};

impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let m = heights.len();
        let n = heights[0].len();

        let mut heap = BinaryHeap::new();
        let mut visited = HashSet::new();

        heap.push(Reverse((0, 0, 0)));

        while !heap.is_empty() {
            let Reverse((effort, x, y)) = heap.pop().unwrap();
            if visited.contains(&(x, y)) {
                continue;
            }

            if x == m - 1 && y == n - 1 {
                return effort;
            }
            visited.insert((x, y));

            for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)].iter() {
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx < 0 || nx >= m as i32 || ny < 0 || ny >= n as i32 {
                    continue;
                }
                let nx = nx as usize;
                let ny = ny as usize;
                let new_effort = (heights[nx][ny] - heights[x][y]).abs().max(effort);
                heap.push(Reverse((new_effort, nx, ny)));
            }
        }

        0
    }
}