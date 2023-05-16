use std::collections::VecDeque;

impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let mut q = VecDeque::from(senate.chars().collect::<Vec<char>>());
        let mut banned_d = 0;
        let mut banned_r = 0;  
        let mut r_count = q.iter().filter(|&c| *c == 'R').count();
        let mut d_count = q.len() - r_count;

        while r_count > 0 && d_count > 0 {
            let c = q.pop_front().unwrap();
            if c == 'R' {
                if banned_r > 0 {
                    banned_r -= 1;
                    r_count -= 1
                } else {
                    q.push_back('R');
                    banned_d += 1;
                }
            } else {
                if banned_d > 0 {
                    banned_d -= 1;
                    d_count -= 1;
                } else {
                    banned_r += 1;
                    q.push_back('D');
                }
            }
        }

        if r_count > 0 {
            "Radiant".to_string()
        } else {
            "Dire".to_string()
        }
    }
}