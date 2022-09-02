#include <vector>
#include <algorithm>
#include <limits>
#include <iostream>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        const int INF = amount + 1;
        vector<int> dp(amount + 1, INF);
        dp[0] = 0;
        for (auto denomination : coins) {
            for (int i = denomination; i <= amount; ++i) {
                dp[i] = min(dp[i], dp[i - denomination] + 1);
            }
        } 
        
        return dp.back() == INF ? -1 : dp.back();
    }
};

int main() {
    Solution s;
    vector<int> coins {1, 2, 5};
    auto res = s.coinChange(coins, 11);
    cout << res << endl;   
    return 0;
}