struct ParkingSystem {
    available: [i32; 3],
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {
    fn new(big: i32, medium: i32, small: i32) -> Self {
        ParkingSystem {
            available: [big, medium, small],
        }
    }
    
    fn add_car(&mut self, car_type: i32) -> bool {
        if self.available[car_type as usize - 1] > 0 {
            self.available[car_type as usize - 1] -= 1;
            return true;
        }
        false
    }
}