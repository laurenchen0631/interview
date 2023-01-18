#include <vector>

using namespace std;

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int sum {0};
        int maxSum {nums[0]}, curMax {0};
        int minSum {nums[0]}, curMin {0};

        for (auto n : nums) {
            sum += n;
            curMax = max(curMax + n, n);
            maxSum = max(maxSum, curMax);
            curMin = min(curMin + n, n);
            minSum = min(minSum, curMin);
        }
        return maxSum > 0 ? max(maxSum, sum - minSum) : maxSum;
    }
};