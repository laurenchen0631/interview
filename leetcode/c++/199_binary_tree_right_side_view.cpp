#include <vector>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (!root) return {};

        vector<int> res;
        queue<TreeNode*> q({root});
        while (!q.empty()) {
            TreeNode* last;
            auto size = q.size();
            for (int i = 0; i < size; ++i) {
                last = q.front();
                q.pop();
                if (last->left) q.push(last->left);
                if (last->right) q.push(last->right);
            }
            res.push_back(last->val);
        }
        return res;
    }
};