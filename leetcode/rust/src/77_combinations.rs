pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
    let mut res = Vec::new();
    let mut path = Vec::new();
    dfs(n, k, 1, &mut path, &mut res);
    res
}

fn dfs(n: i32, k: i32, start: i32, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
    if path.len() == k as usize {
        res.push(path.clone());
        return;
    }
    for i in start..=n {
        path.push(i);
        dfs(n, k, i + 1, path, res);
        path.pop();
    }
}