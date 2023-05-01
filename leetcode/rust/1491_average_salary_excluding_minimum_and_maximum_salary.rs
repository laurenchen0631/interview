use std::cmp;

impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let mut min = salary[0];
        let mut max = salary[0];
        let mut sum = 0;
        for s in &salary {
            sum += *s;
            min = cmp::min(min, *s);
            max = cmp::max(max, *s);
        }
        (sum - min - max) as f64 / (salary.len() - 2) as f64
    }
}