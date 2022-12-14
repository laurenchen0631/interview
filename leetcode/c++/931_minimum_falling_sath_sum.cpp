#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        vector<int> dp(matrix[0].size(), 0);
        for (auto row : matrix) {
            vector<int> temp(row.size(), 0);
            for (int i = 0; i < row.size(); i++) {
                temp[i] = row[i] + dp[i];
                if (i > 0) {
                    temp[i] = min(temp[i], row[i] + dp[i - 1]);
                }
                if (i < row.size() - 1) {
                    temp[i] = min(temp[i], row[i] + dp[i + 1]);
                }
            }
            dp = temp;
        }
        return *min_element(dp.begin(), dp.end());
    }
};