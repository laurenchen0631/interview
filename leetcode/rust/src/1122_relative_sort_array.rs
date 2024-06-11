impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        let mut arr1 = arr1;
        let mut arr2 = arr2;
        let mut arr1_count = vec![0; 1001];
        let mut result = Vec::new();
        for i in 0..arr1.len() {
            arr1_count[arr1[i] as usize] += 1;
        }
        for i in 0..arr2.len() {
            while arr1_count[arr2[i] as usize] > 0 {
                result.push(arr2[i]);
                arr1_count[arr2[i] as usize] -= 1;
            }
        }
        for i in 0..1001 {
            while arr1_count[i] > 0 {
                result.push(i as i32);
                arr1_count[i] -= 1;
            }
        }
        result
    }
}
