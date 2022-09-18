#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int l {0};
        int r = height.size() - 1;
        int lMax {0}, rMax {0};
        int res {0};
        while (l < r) {
            if (height[l] < height[r]) {
                if (height[l] < lMax)
                    res += lMax - height[l];
                else
                    lMax = height[l];
                ++l;
            }
            else {
                if (height[r] < rMax)
                    res += rMax - height[r];
                else
                    rMax = height[r];
                --r;
            }
        }
        return res;
    }
};

int main() {
    return 0;
}