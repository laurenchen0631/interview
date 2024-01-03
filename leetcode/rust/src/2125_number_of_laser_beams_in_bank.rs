impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let mut prev = 0;
        let mut res = 0;

        for row in bank {
            let mut devices = 0;
            for c in row.chars() {
                if c == '1' {
                    devices += 1;
                }
            }

            if devices > 0 {
                res += prev * devices;
                prev = devices;
            }
        }
        res
    }
}