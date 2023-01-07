#include <vector>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int needed {0};
        int tank {0};
        int start {-1};
        for (int i = 0; i < gas.size(); i++) {
            int t = tank + gas[i] - cost[i];
            if (t < 0) {
                needed += t;
                tank = 0;
                start = -1;
            }
            else {
                if (start == -1) {
                    start = i;
                }
                tank = t;
            }
        }
        return tank + needed >= 0 ? start : -1;
    }
};