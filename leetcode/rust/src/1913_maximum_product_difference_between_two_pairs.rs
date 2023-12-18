impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let mut first_min = i32::MAX;
        let mut second_min = i32::MAX;
        let mut first_max = 0;
        let mut second_max = 0;

        for n in nums.iter() {
            if *n < first_min {
                second_min = first_min;
                first_min = *n;
            } else if *n < second_min {
                second_min = *n;
            }

            if *n > first_max {
                second_max = first_max;
                first_max = *n;
            } else if *n > second_max {
                second_max = *n;
            }
            
        }

        return first_max * second_max - first_min * second_min;
    }
}