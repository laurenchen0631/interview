use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut lose_count = HashMap::new();
        let mut players = HashSet::new();

        for pair in matches {
            let winner = pair[0];
            let loser = pair[1];

            players.insert(winner);
            players.insert(loser);
            lose_count.entry(loser).and_modify(|f| *f += 1).or_insert(1);
        }

        let mut no_lose = Vec::new();
        let mut one_lose = Vec::new();
        let mut players = players.into_iter().collect::<Vec<i32>>();
        players.sort_unstable();
        for player in players {
            match lose_count.get(&player) {
                None => no_lose.push(player),
                Some(1) => one_lose.push(player),
                _ => (),
            }
        }
        vec![no_lose, one_lose]
    }
}