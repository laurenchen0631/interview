impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left = vec![0; height.len()];
        let mut right = vec![0; height.len()];
        for i in 1..height.len() {
            left[i] = left[i - 1].max(height[i - 1]);
        }

        for i in (0..height.len() - 1).rev() {
            right[i] = right[i + 1].max(height[i + 1]);
        }

        let mut res = 0;
        for i in 0..height.len() {
            let min = left[i].min(right[i]);
            if min > height[i] {
                res += min - height[i];
            }
        }
        res
    }
}
