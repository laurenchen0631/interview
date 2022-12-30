#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> path = {0};
        dfs(graph, 0, path);
        return res;
    }

    void dfs(vector<vector<int>>& graph, int node, vector<int>& path) {
        if (node == graph.size() - 1) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < graph[node].size(); i++) {
            path.push_back(graph[node][i]);
            dfs(graph, graph[node][i], path);
            path.pop_back();
        }
    }
private:
    vector<vector<int>> res;
};