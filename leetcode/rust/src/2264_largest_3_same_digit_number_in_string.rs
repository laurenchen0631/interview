impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let mut l = 0;
        let mut prev: char = ' ';
        let mut res = "";
        for (r, c) in num.chars().enumerate() {
            if c != prev {
                l = r;
                prev = c;
            }
            else if r - l + 1 == 3 {
                let tmp = &num[l..=r];
                
                if res.len() == 0 {
                    res = tmp;
                }
                else {
                    if res < tmp {
                        res = tmp;
                    }
                }
            }
        }
        return String::from(res);
    }
}