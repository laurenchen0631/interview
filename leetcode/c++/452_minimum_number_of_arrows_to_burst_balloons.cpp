#include <vector>

using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0) return 0;

        sort(points.begin(), points.end(), [](vector<int> a, vector<int> b) {
            return a[1] < b[1];
        });

        int count {1};
        int curEnd {points[0][1]};
        for (auto p : points) {
            auto start = p[0];
            auto end = p[1];
            if (curEnd < start) {
                count++;
                curEnd = end;
            }
        }
        return count;
    }
};