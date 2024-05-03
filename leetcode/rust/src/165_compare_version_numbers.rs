impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let v1: Vec<i32> = version1.split('.').map(|s| s.parse().unwrap()).collect();
        let v2: Vec<i32> = version2.split('.').map(|s| s.parse().unwrap()).collect();
        let n = v1.len().max(v2.len());
        for i in 0..n {
            let a = v1.get(i).unwrap_or(&0);
            let b = v2.get(i).unwrap_or(&0);
            if a < b {
                return -1;
            } else if a > b {
                return 1;
            }
        }
        0
    }
}
