impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let k = ((arr.len() as f32) / 4.0).floor() as usize;
        for i in 0..arr.len() - k {
            if arr[i] == arr[i + k] {
                return arr[i];
            }
        }
        -1
    }
}