impl Solution {
    pub fn min_cost_ii(costs: Vec<Vec<i32>>) -> i32 {
        let mut costs = costs;
        let n = costs.len();
        let k = costs[0].len();
        for i in 1..n {
            let mut min_color = 0;
            let mut second_min_color = 0;
            for color in 1..k {
                if costs[i-1][color] < costs[i-1][min_color] {
                    second_min_color = min_color;
                    min_color = color;
                } else if min_color == second_min_color || costs[i-1][color] < costs[i-1][second_min_color] {
                    second_min_color = color;
                }
            }

            for color in 0..k {
                if color == min_color {
                    costs[i][color] += costs[i - 1][second_min_color];
                } else {
                    costs[i][color] += costs[i - 1][min_color];
                }
            }
        }
        *costs[n - 1].iter().min().unwrap()
    }
}