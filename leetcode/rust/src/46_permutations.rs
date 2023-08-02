impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        let mut path = Vec::new();
        Solution::dfs(&nums, &mut path, &mut res);
        res
    }

    fn dfs(nums: &Vec<i32>, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        if path.len() == nums.len() {
            res.push(path.clone());
            return;
        }
        for i in 0..nums.len() {
            if path.contains(&nums[i]) {
                continue;
            }
            path.push(nums[i]);
            Solution::dfs(nums, path, res);
            path.pop();
        }
    }
}