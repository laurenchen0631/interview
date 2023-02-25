#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int curMin = prices[0];
        int maxProfit = 0;
        for (auto price : prices) {
            if (price < curMin) {
                curMin = price;
            } else {
                maxProfit = max(maxProfit, price - curMin);
            }
        }
        return maxProfit;
    }
};