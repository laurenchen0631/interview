impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        // bellman-ford
        let n = n as usize;
        let mut dist = vec![std::i32::MAX; n];
        dist[src as usize] = 0;

        for _ in 0..k + 1 {
            let mut tmp = dist.clone();
            for flight in &flights {
                let u = flight[0] as usize;
                let v = flight[1] as usize;
                let w = flight[2];
                if dist[u] != std::i32::MAX && dist[u] + w < tmp[v] {
                    tmp[v] = dist[u] + w;
                }
            }
            dist = tmp;
        }

        if dist[dst as usize] == std::i32::MAX {
            -1
        } else {
            dist[dst as usize]
        }

    }
}