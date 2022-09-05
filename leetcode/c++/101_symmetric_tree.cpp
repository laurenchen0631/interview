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
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) return true;
        return isSymmetric(root->left, root->right);
    }

    bool isSymmetric(TreeNode* l, TreeNode* r) {
        if (!l || !r) return l == r;
        return l->val == r->val 
            && isSymmetric(l->left, r->right)
            && isSymmetric(l->right, r->left);
    }
};