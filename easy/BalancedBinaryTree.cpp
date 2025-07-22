#include <cstdlib>
#include <iostream>

using namespace std;
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  bool isBalanced(TreeNode *root) {
    if (!root)
      return false;

    if (abs((1 + isBalanced(root->right)) - (1 + isBalanced(root->left))) > 1) {
      return false;
    }
    return true;
  }
};

int main() {

  Solution s = Solution();
  TreeNode t = TreeNode(0);
  TreeNode *temp = &t;

  for (int i = 1; i < 6; i++) {
    temp->left = new TreeNode(i);
    temp->right = new TreeNode(i + 1);
    temp = temp->left;
  }
  cout << s.isBalanced(&t);
}
