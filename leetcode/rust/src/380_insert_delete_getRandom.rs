use std::collections::HashMap;
use rand::seq::SliceRandom;

struct RandomizedSet {
    list: Vec<i32>,
    map: HashMap<i32, usize>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        return RandomizedSet {
            list: Vec::new(),
            map: HashMap::new(),
        }
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if self.map.contains_key(&val) {
            return false;
        }

        self.map.insert(val, self.list.len());
        self.list.push(val);
        return true;
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if !self.map.contains_key(&val) {
            return false;
        }

        let index = self.map.get(&val).unwrap().clone();
        let last = self.list.last().unwrap().clone();
        self.map.insert(last, index);
        self.list[index] = last;
        self.list.pop();
        self.map.remove(&val);
        return true;
    }
    
    fn get_random(&self) -> i32 {
        self.list.choose(&mut rand::thread_rng()).unwrap().clone()
    }
}

