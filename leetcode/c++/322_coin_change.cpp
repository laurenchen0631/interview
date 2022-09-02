#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int maxSteal {0};
        int maxSkip {0};
        for (auto n : nums) {
            auto curMax = max(maxSteal, maxSkip + n);
            maxSkip = maxSteal;
            maxSteal = curMax;
        }
        return maxSteal;
    }
};

int main() {
    Solution s;
    vector<int> nums {2, 7, 9, 3, 1};
    auto res = s.rob(nums);
    cout << res << endl;
    return 0;
}