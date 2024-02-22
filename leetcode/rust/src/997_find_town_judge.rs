impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let mut trust_count = vec![0; n as usize];
        for t in trust {
            trust_count[t[0] as usize - 1] -= 1;
            trust_count[t[1] as usize - 1] += 1;
        }
        for i in 0..n as usize {
            if trust_count[i] == n - 1 {
                return i as i32 + 1;
            }
        }
        -1
    }
}