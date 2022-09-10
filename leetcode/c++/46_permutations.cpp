#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        helper(nums, 0, res);
        return res;
    }

    void helper(vector<int>& nums, int l, vector<vector<int>>& res) {
        if (l == nums.size()) {
            return res.push_back(nums);
        }

        for (int i = l; i < nums.size(); i++) {
            swap(nums[l], nums[i]);
            helper(nums, l + 1, res);
            swap(nums[l], nums[i]);
        }
    }
};