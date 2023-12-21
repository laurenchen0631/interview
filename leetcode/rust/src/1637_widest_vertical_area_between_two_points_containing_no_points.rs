impl Solution {
    pub fn max_width_of_vertical_area(points: Vec<Vec<i32>>) -> i32 {
        let mut points = points;
        points.sort_unstable_by_key(|v| v[0]);
        let mut res = 0;
        for i in 1..points.len() {
            res = res.max(points[i][0] - points[i-1][0]);
        }
        res
    }
}