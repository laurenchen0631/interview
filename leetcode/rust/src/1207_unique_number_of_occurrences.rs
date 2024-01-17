use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let count = arr.iter().fold(
            HashMap::new(), 
            |mut acc, &x| {
                *acc.entry(x).or_insert(0) += 1;
                acc
            });

        let occurrences = count.values().into_iter().fold(
            HashSet::new(), 
            |mut acc, &x| {
                acc.insert(x);
                acc
            });

        occurrences.len() == count.len()
    }
}