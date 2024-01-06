impl Solution {
    pub fn job_scheduling(start_time: Vec<i32>, end_time: Vec<i32>, profit: Vec<i32>) -> i32 {
        let n = start_time.len();
        let mut jobs = (0..n)
            .map(|i| (start_time[i], end_time[i], profit[i]))
            .collect::<Vec<_>>();
        let mut dp = vec![0; n+1];
        
        for i in (0..n).rev() {
            let (s, e, p) = jobs[i];
            let j = (i+1..n).find(|&j| jobs[j].0 >= e).unwrap_or(n);

           
            dp[i] = dp[i+1].max(dp[j] + p);
        }
        dp[0]

    }
}
