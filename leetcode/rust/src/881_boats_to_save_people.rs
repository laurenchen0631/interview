impl Solution {
    pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 {
        let mut people = people;
        people.sort_unstable();
        let mut i = 0;
        let mut j = people.len() - 1;
        let mut boats = 0;
        while i <= j {
            if people[i] + people[j] <= limit {
                i += 1;
            }
            boats += 1;

            // handle usize underflow
            if j > 0 {
                j -= 1;
            }
            else {
                break;
            }
        }
        boats
    }
}
