use std::collections::HashSet;

impl Solution {

    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        let mut set = HashSet::new();
        for path in paths.iter() {
            set.insert(&path[0]);
        }
        for path in paths.iter() {
            if !set.contains(&path[1]) {
                return path[1].clone();
            }
        }
        String::new()
    }
}