pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
    let n = grid.len();
    if grid[0][0] == 1 || grid[n - 1][n - 1] == 1 {
        return -1;
    }
    let mut grid = grid;
    grid[0][0] = 1;
    let mut queue = vec![(0, 0)];
    let mut steps = 1;
    while !queue.is_empty() {
        let mut next = vec![];
        for (i, j) in queue {
            if i == n - 1 && j == n - 1 {
                return steps;
            }
            for (x, y) in vec![
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ] {
                if x < n && y < n && grid[x][y] == 0 {
                    grid[x][y] = 1;
                    next.push((x, y));
                }
            }
        }
        queue = next;
        steps += 1;
    }
    -1
}