impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        let mut first_min = i32::MAX;
        let mut second_min = i32::MAX;
        for price in prices {
            if price < first_min {
                second_min = first_min;
                first_min = price;
            } else if price < second_min {
                second_min = price;
            }
        }

        if first_min + second_min > money {
            return money;
        }
        money - first_min - second_min
    }
}