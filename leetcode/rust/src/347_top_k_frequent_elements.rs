use std::collections::{HashMap, BinaryHeap};

pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let frequencies = nums
          .iter()
          .copied()
          .fold(HashMap::new(), |mut map, val|{
              map.entry(val)
                 .and_modify(|frq|*frq+=1)
                 .or_insert(1);
              map
          });

    let frequencies: Vec<(i32, i32)> = frequencies
        .into_iter()
        .map(|v| (v.1, v.0))
        .collect();
    let mut heap = BinaryHeap::from(frequencies);

    let mut res = vec![];
    for _ in 0..k {
        let (_, key) = heap.pop().unwrap();
        res.push(key);
    }
    res
}