#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        auto n {prices.size()};
        if (!n || k == 0) return 0;
        if (2 * k > n) return maxProfit(prices);

        int dp[n][k + 1][2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i][j][0] = -1000;
                dp[i][j][1] = -1000;
            }
        }
        dp[0][0][0] = 0;
        dp[0][1][1] = -prices[0];
        
        for (int d = 1; d < n; d++) {
            for (int j=0; j <= k; j++) {
                dp[d][j][0] = max(dp[d-1][j][0], dp[d-1][j][1] + prices[d]);
                if (j > 0) dp[d][j][1] = max(dp[d-1][j][1], dp[d-1][j-1][0] - prices[d]);
            }
        }
        int res {0};
        for (int j = 0; j <= k; j++) res = max(res, dp[n-1][j][0]);
        return res;
    }

    int maxProfit(vector<int>& prices) {
        int res {0};
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] > prices[i-1]) res += prices[i] - prices[i-1];
        }
        return res;
    }
};