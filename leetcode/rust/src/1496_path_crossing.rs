use std::collections::HashSet;

impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        let mut pos = (0, 0);
        let mut visited = HashSet::new();
        for c in path.chars() {
            visited.insert(pos);
            match c {
                'N' => pos.1 += 1,
                'S' => pos.1 -= 1,
                'E' => pos.0 += 1,
                'W' => pos.0 -= 1,
                _ => (),
            }
            if visited.contains(&pos) {
                return true;
            }
        }
        
        false
    }
}