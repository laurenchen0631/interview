pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
    let mut visited = vec![false; is_connected.len()];
    let mut count = 0;
    for i in 0..is_connected.len() {
        if !visited[i] {
            dfs(&is_connected, &mut visited, i);
            count += 1;
        }
    }
    count
}

pub fn dfs(is_connected: &Vec<Vec<i32>>, visited: &mut Vec<bool>, i: usize) {
    for j in 0..is_connected.len() {
        if is_connected[i][j] == 1 && !visited[j] {
            visited[j] = true;
            dfs(is_connected, visited, j);
        }
    }
}
