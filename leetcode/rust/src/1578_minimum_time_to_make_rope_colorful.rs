impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut i = 0;
        while i < colors.len() {
            let mut cur_max = 0;
            let color = &colors[i..i+1];

            while i < colors.len() && &colors[i..i+1] == color {
                cur_max = cur_max.max(needed_time[i]);
                res += needed_time[i];
                i += 1;
            }
            res -= cur_max;
        }
        res
    }
}