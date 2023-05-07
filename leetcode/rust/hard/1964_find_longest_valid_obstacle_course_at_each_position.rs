impl Solution {
    pub fn longest_obstacle_course_at_each_position(obstacles: Vec<i32>) -> Vec<i32> {
        let mut res = vec![];
        let mut seq = vec![];
        for o in obstacles {
            let i = seq.partition_point(|&x| x <= o);
            if i == seq.len() {
                seq.push(o);
            } else {
                seq[i] = o;
            }
            res.push((i + 1) as i32);
        }
        res
            
    }
}