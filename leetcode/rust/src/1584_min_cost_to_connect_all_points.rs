impl Solution {
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut res = 0;
        let mut edges = 0;
        let mut visited = vec![false; n];

        let mut dist = vec![i32::MAX; n];
        dist[0] = 0;
        let mut cur = 0;

        while edges < n {
            println!("{}", cur);
            res += dist[cur];
            edges += 1;
            visited[cur] = true;

            let mut cur_min = i32::MAX;
            let mut next_node = cur;
            for i in 0..n {
                if visited[i] {
                   continue; 
                }
                let d = (points[cur][0] - points[i][0]).abs() + (points[cur][1] - points[i][1]).abs();
                dist[i] = dist[i].min(d);
                if dist[i] < cur_min {
                    next_node = i;
                    cur_min = dist[i];
                }
            }
            cur = next_node;
        }
        res
    }
}