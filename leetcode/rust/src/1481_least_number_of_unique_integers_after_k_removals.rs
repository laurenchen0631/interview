impl Solution {
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, k: i32) -> i32 {
        let count = arr
            .iter()
            .fold(
                std::collections::HashMap::new(), 
                |mut acc, &x| {
                    *acc.entry(x).or_insert(0) += 1;
                    acc
            });
        
        let mut pairs = count
            .iter()
            .map(|(&k, &v)| (v, k))
            .collect::<Vec<_>>();

        pairs.sort_unstable();

        let mut k = k;
        let mut res = pairs.len() as i32;
        for (i, (v, _)) in pairs.iter().enumerate() {
            if k >= *v {
                k -= *v;
                res -= 1;
            } else {
                break;
            }
        }
        
        res
    }
}