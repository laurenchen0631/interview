impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        for i in 1..points.len() {
            let p1 = points.get(i-1).unwrap();
            let p2 = points.get(i).unwrap();
            res += (p1[0] - p2[0]).abs().max((p1[1] - p2[1]).abs())
        }
        res
    }
}