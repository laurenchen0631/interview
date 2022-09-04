#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res {nums[0] + nums[1] + nums[2]};
        for (int i = 0; i < size(nums); ++i) {
            int l {i + 1}, r = size(nums) - 1;
            while (l < r) {
                auto sum {nums[i] + nums[l] + nums[r]};
                if (abs(sum - target) < abs(res - target)) {
                    res = sum;
                }

                if (sum > target) r -= 1;
                else if (sum < target) l += 1;
                else return res;
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> nums {-1, 2, 1, -4};
    auto res = s.threeSumClosest(nums, 1);
    return 0;
}