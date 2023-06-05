pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
    let [x1, y1] = [coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]];
    for i in 2..coordinates.len() {
        let [x2, y2] = [coordinates[i][0] - coordinates[0][0], coordinates[i][1] - coordinates[0][1]];
        if x1 * y2 != x2 * y1 {
            return false;
        }
    }
    true
}
