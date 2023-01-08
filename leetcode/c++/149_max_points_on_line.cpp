#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        if (points.size() <= 2) return points.size();
        int res {0};
        for (int i = 0; i < points.size(); i++) {
            unordered_map<double, int> cnt;
            for (int j = 0; j < points.size(); j++) {
                if (i == j) continue;
                double k = atan2(points[j][1] - points[i][1], points[j][0] - points[i][0]);
                cnt[k]++;
            }
            for (auto [d, c] : cnt) {
                res = max(res, c + 1);
            }
        }
        return res;
    }
};