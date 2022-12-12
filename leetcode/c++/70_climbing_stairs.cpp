class Solution {
public:
    int climbStairs(int n) {
        int dp[2] {1, 2};
        if (n <= 2) {
            return dp[n - 1];
        }
        for (auto i=3; i<=n; ++i) {
            auto tmp {dp[1]};
            dp[1] += dp[0];
            dp[0] = tmp;
        }
        return dp[1];
    }
};