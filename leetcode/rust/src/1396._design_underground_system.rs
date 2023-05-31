use std::collections::HashMap;

struct UndergroundSystem {
    check_in: HashMap<i32, (String, i32)>,
    records: HashMap<(String, String), [i32;2]>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl UndergroundSystem {
    fn new() -> Self {
        UndergroundSystem {
            check_in: HashMap::new(),
            records: HashMap::new(),
        }
    }
    
    fn check_in(&mut self, id: i32, station_name: String, t: i32) {
        self.check_in.insert(id, (station_name, t));
    }
    
    fn check_out(&mut self, id: i32, station_name: String, t: i32) {
        let check_in = self.check_in.remove(&id).unwrap();
        let key = (check_in.0, station_name);
        let record = self.records.entry(key).or_insert([0, 0]);
        record[0] += t - check_in.1;
        record[1] += 1;
    }
    
    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        let key = (start_station, end_station);
        let record = self.records.get(&key).unwrap();
        record[0] as f64 / record[1] as f64
    }
}