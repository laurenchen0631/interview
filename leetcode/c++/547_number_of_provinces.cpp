#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        auto n {isConnected.size()};
        vector<int> parent(n, -1);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (isConnected[i][j] == 1 && i != j) {
                    unionSet(parent, i, j);
                }
            }
        }

        int res {0};
        for (int i=0; i < n; i++) {
            if (parent[i] == -1) {
                res++;
            }
        }
        return res;
    }

    void unionSet(vector<int>& parent, int i, int j) {
        int pi = find(parent, i);
        int pj = find(parent, j);
        if (pi != pj) {
            parent[pi] = pj;
        }
    }

    int find(vector<int>& parent, int i) {
        if (parent[i] == -1) {
            return i;
        }
        return find(parent, parent[i]);
    }
};