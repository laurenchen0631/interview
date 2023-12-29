use std::collections::HashMap;

impl Solution {
    pub fn min_difficulty(job_difficulty: Vec<i32>, d: i32) -> i32 {
        if d as usize > job_difficulty.len() {
            return -1;
        }

        let mut task = JobSchedule::new(job_difficulty, d as usize);
        task.min_difficulty(0, d as usize)
    }
}

struct JobSchedule {
    cache: HashMap<(usize, usize), i32>,
    base: Vec<i32>,
    job_difficulty: Vec<i32>,
    days: usize,
}

impl JobSchedule {
    pub fn new(job_difficulty: Vec<i32>, days: usize) -> Self {
        let mut base = vec![job_difficulty.last().unwrap().clone(); job_difficulty.len() + 1];
        for i in (0..job_difficulty.len()-1).rev() {
            base[i] = base[i + 1].max(job_difficulty.get(i).unwrap().clone());
        }
 
        Self {
            cache: HashMap::new(),
            base,
            job_difficulty,
            days,
        }
    }

    pub fn min_difficulty(&mut self, i: usize, days: usize) -> i32 {
        if days == 1 {
            return self.base[i];
        }

        if let Some(&v) = self.cache.get(&(i, days)) {
            return v;
        }

        let mut res = std::i32::MAX;
        let mut max = 0;
        for j in i..self.job_difficulty.len() - days + 1 {
            max = max.max(self.job_difficulty[j]);
            res = res.min(max + self.min_difficulty(j + 1, days - 1));
        }

        self.cache.insert((i, days), res);
        res
    }
    
}