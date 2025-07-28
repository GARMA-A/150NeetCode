#include <cstdlib>
#include <iostream>
#include <system_error>

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
  bool isBalanced(TreeNode *root) { return DFS(root).first; }

  pair<bool, int> DFS(TreeNode *root) {
    if (not root) {
      return {true, 0};
    }
    pair<bool, int> left = DFS(root->left), right = DFS(root->right);
    bool balanced =
        (left.first and right.first and abs(left.second - right.second) <= 1);
    return {balanced, 1 + max(left.second, right.second)};
  }
};
