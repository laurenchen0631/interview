
pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
    let mut dp = vec![0; stone_value.len() + 1];
    for i in (0..stone_value.len()).rev() {
        dp[i] = stone_value[i] - dp[i + 1];
        if i + 2 <= stone_value.len() {
            dp[i] = std::cmp::max(
                dp[i],
                stone_value[i] + stone_value[i + 1] - dp[i + 2],
            );
        }

        if i + 3 <= stone_value.len() {
            dp[i] = std::cmp::max(
                dp[i],
                stone_value[i] + stone_value[i + 1] + stone_value[i + 2]
                    - dp[i + 3],
            );
        }
    }

    if dp[0] > 0 {
        "Alice".to_string()
    } else if dp[0] < 0 {
        "Bob".to_string()
    } else {
        "Tie".to_string()
    }
}