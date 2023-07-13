
use std::collections::VecDeque;

pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
    let mut adj = vec![vec![]; num_courses as usize];
    let mut incoming = vec![0; num_courses as usize];
    for p in prerequisites {
        adj[p[1] as usize].push(p[0] as usize);
        incoming[p[0] as usize] += 1;
    }


    let mut q = VecDeque::new();
    for i in 0..num_courses as usize {
        if incoming[i] == 0 {
            q.push_back(i);
        }
    }

    let mut count = 0;
    while q.len() > 0 {
        let u = q.pop_front().unwrap();
        count += 1;
        for &v in &adj[u] {
            incoming[v] -= 1;
            if incoming[v] == 0 {
                q.push_back(v);
            }
        }
    }
    return count == num_courses;
}