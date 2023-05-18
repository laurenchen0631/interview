
impl Solution {
    pub fn find_smallest_set_of_vertices(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let mut indegree = vec![0; n as usize];
        for edge in edges {
            indegree[edge[1] as usize] += 1;
        }

        indegree
            .iter()
            .enumerate()
            .filter(|(_, &x)| x == 0)
            .map(|(i, _)| i as i32)
            .collect()

    }
}