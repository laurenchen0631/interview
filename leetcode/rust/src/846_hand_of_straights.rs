use std::collections::HashMap;

impl Solution {
    pub fn is_n_straight_hand(hand: Vec<i32>, group_size: i32) -> bool {
        let mut hand = hand;
        hand.sort_unstable();
        let mut map = HashMap::new();

        for i in &hand {
            *map.entry(*i).or_insert(0) += 1;
        }
        
        for i in hand {
            if map[&i] > 0 {
                for j in 0..group_size {
                    if let Some(x) = map.get_mut(&(i + j)) {
                        if *x == 0 {
                            return false;
                        }
                        *x -= 1;
                    } else {
                        return false;
                    }
                }
            }
        }
        true
    }
}
