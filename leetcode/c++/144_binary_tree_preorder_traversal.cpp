#include <vector>

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
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> res;
        vector<TreeNode*> stack({root});
        while (!stack.empty()) {
            auto p {stack.back()};
            stack.pop_back();
            if (p->right) stack.push_back(p->right);
            if (p->left) stack.push_back(p->left);
            res.push_back(p->val);
        }
        return res;
    }
};