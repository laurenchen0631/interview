#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int curMax {nums[0]}, curMin {nums[0]}, res {nums[0]};
        for (int i = 1; i < size(nums); ++i) {
            auto n {nums[i]};
            curMax *= n;
            curMin *= n;
            if (n < 0) {
                swap(curMax, curMin);
            }
            curMax = max(curMax, n);
            curMin = min(curMin, n);
            res = max(res, curMax);
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> nums {2, 3, -2, 4};
    auto res = s.maxProduct(nums);
    cout << res << endl;
    return 0;
}
