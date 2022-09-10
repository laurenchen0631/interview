#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        helper(candidates, target, 0, {}, res);
        return res;
    }

    void helper(vector<int>& candidates, int target, int l, vector<int> comb, vector<vector<int>>& res) {
        if (target == 0) {
            return res.push_back(comb);
        }

        for (int i = l; i < candidates.size(); i++) {
            if (candidates[i] > target) {
                break;
            }
            comb.push_back(candidates[i]);
            helper(candidates, target - candidates[i], i, comb, res);
            comb.pop_back();
        }
    }
};

int main() {
    Solution s;
    vector<int> candidates = {2, 3, 6, 7};
    int target = 7;
    auto res = s.combinationSum(candidates, target);
    return 0;
}