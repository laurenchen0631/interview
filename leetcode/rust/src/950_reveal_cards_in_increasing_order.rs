use std::collections::VecDeque;

impl Solution {
    // [17,13,11,2,3,5,7] -> [2,3,5,7,11,13,17]
    // -> [2,13,3,11,5,17,7]
    pub fn deck_revealed_increasing(deck: Vec<i32>) -> Vec<i32> {
        let mut deck = deck;
        deck.sort_unstable();
        let mut queue = VecDeque::new();
        for i in (0..deck.len()).rev() {
            if !queue.is_empty() {
                let last = queue.pop_back().unwrap();
                queue.push_front(last);
            }
            queue.push_front(deck[i]);
            // [17]
            // [13, 17]
            // [11, 17, 13]
            // [7, 13, 11, 17]
            // [5, 17, 7, 13, 11]
            // [3, 11, 5, 17, 7, 13]
            // [2, 13, 3, 11, 5, 17, 7]
        }
        queue.into_iter().collect()
    }
}