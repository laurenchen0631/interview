#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int maxPos = 0;
        int i = 0;
        while (i <= maxPos) {
            maxPos = max(maxPos, i + nums[i]);
            if (maxPos >= n - 1) {
                return true;
            }
            i++;
        }

        return false;
    }
};