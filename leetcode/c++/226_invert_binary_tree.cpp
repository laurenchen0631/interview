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
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return root;

        vector<TreeNode*> stack = {root};
        while (!stack.empty()) {
            TreeNode* node = stack.back();
            stack.pop_back();
            if (node == nullptr) continue;
            swap(node->left, node->right);
            stack.push_back(node->left);
            stack.push_back(node->right);
        }
        return root;
    }
};