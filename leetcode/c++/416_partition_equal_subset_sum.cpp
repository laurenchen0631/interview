
#include <vector>
#include <numeric>
#include <iostream>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total {accumulate(nums.begin(), nums.end(), 0)};
        if (total & 1) return false;

        auto target = total / 2;
        auto n {nums.size()};
        bool dp[n+1][target+1];
        dp[0][0] = true;

        for (int i = 1; i <= n; ++i) {
            auto cur {nums[i-1]};
            for (int j = 1; j <= target; ++j) {
                if (j < cur) 
                    dp[i][j] = dp[i-1][j];
                else
                    dp[i][j] = dp[i-1][j] || dp[i-1][j-cur];
            }
        }
        return dp[n][target];
    }
};

int main() {
    Solution s;
    vector<int> nums {1, 5, 11, 5};
    auto res = s.canPartition(nums);
    cout << res << endl;
    return 0;
}