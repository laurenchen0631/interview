#include <queue>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

using namespace std;

class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        int res = 0;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        while (!q.empty()) {
            int size = q.size();
            int left = q.front().second;
            int right = q.back().second;
            res = max(res, right - left + 1);
            for (int i = 0; i < size; i++) {
                auto node = q.front().first;
                auto index = q.front().second;
                int idx = index - left;
                q.pop();
                if (node->left) {
                    q.push({node->left, (long long)2 * idx});
                }
                if (node->right) {
                    q.push({node->right, (long long)2 * idx + 1});
                }
            }
        }
        return res;
    }
};