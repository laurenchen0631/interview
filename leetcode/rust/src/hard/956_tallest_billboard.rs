use std::{collections::HashMap, cmp};

pub fn tallest_billboard(rods: Vec<i32>) -> i32 {
    let mut dp = HashMap::new();
    dp.insert(0, 0);
    for h in rods {
        for (&k, &v) in dp.clone().iter() {
            // k + h: put h in the longer side
            dp.entry(k + h)
                .and_modify(|x| *x = (*x).max(v))
                .or_insert(v);
            dp.entry((k - h).abs())
                .and_modify(|x| *x = (*x).max(v + cmp::min(k, h)))
                .or_insert(v + cmp::min(k, h));
        }
    }

    return *dp.get(&0).unwrap();
}