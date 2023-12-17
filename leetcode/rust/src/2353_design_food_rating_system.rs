use std::{collections::{HashMap, BinaryHeap}, cmp::Reverse};

struct FoodRatings {
    heaps: HashMap<String, BinaryHeap<(i32, Reverse<String>)>>,
    ratings: HashMap<String, i32>,
    cuisines: HashMap<String, String>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FoodRatings {

    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        let mut inst = Self {
            heaps: HashMap::new(),
            ratings: HashMap::new(),
            cuisines: HashMap::new(),
        };

        for i in 0..foods.len() {
            let food = foods[i].clone();
            let cuisine = cuisines[i].clone();
            let rating = ratings[i];
            if !inst.heaps.contains_key(&cuisine) {
                inst.heaps.insert(cuisine.clone(), BinaryHeap::new());
            }

            inst.heaps
                .get_mut(&cuisine).unwrap()
                .push((rating, Reverse(food.clone())));
            inst.ratings.insert(food.clone(), rating);
            inst.cuisines.insert(food.clone(), cuisine);
        }
        inst
    }
    
    fn change_rating(&mut self, food: String, new_rating: i32) {
        self.ratings.insert(food.clone(), new_rating);
        let cuisine = &self.cuisines[&food];
        self.heaps
            .get_mut(cuisine).unwrap()
            .push((new_rating, Reverse(food.clone())));

        // self.heaps[cuisine].push((new_rating, food.clone()));
    }
    
    fn highest_rated(&mut self, cuisine: String) -> String {
        while !self.heaps[&cuisine].is_empty() {
            let (rating, Reverse(food)) = self.heaps[&cuisine].peek().unwrap();
            if self.ratings[food] == *rating {
                return food.clone();
            } else {
                self.heaps.get_mut(&cuisine).unwrap().pop();
            }
        }

        "".to_string()
    }
}
