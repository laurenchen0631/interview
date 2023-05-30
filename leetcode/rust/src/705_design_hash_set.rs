struct MyHashSet {
    // buckets
    buckets: Vec<Vec<i32>>,
    size: usize,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {
    fn new() -> Self {
        let size = 1000;
        Self {
            size,
            buckets: vec![vec![]; size],
        }
    }

    fn hash(&self, key: i32) -> usize {
        key as usize % self.size
    }

    fn expand(&mut self) {
        let old_size = self.size;
        self.size *= 2;
        let mut new_buckets = vec![vec![]; self.size];
        for i in 0..old_size {
            for key in &self.buckets[i] {
                let hash = self.hash(*key);
                if !new_buckets[hash].contains(key) {
                    new_buckets[hash].push(*key);
                }
            }
        }
        self.buckets = new_buckets;
    }
    
    pub fn add(&mut self, key: i32) {
        let hash = self.hash(key);
        if !self.buckets[hash].contains(&key) {
            self.buckets[hash].push(key);
        }

        // increase size if needed
        if self.buckets[hash].len() > self.size / 2 {
            self.expand();
        }
    }
    
    pub fn remove(&self, key: i32) {
        let hash = self.hash(key);
        if let Some(index) = self.buckets[hash].iter().position(|&x| x == key) {
            self.buckets[hash].remove(index);
        }
    }
    
    pub fn contains(&self, key: i32) -> bool {
        let hash = self.hash(key);
        self.buckets[hash].contains(&key)
    }
}
