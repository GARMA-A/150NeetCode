#include <ios>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
  string current_combination;
  vector<string> ans;

public:
  vector<string> generateParenthesis(int n) {
    ans.clear();
    current_combination.clear();

    this->combinations(n, 0, 0);
    return ans;
  }
  void combinations(int n, int left, int right) {
    if (current_combination.size() == n * 2) {
      ans.push_back(current_combination);
      return;
    }
    if (right < left) {
      current_combination.push_back(')');
      combinations(n, left, right + 1);
      current_combination.pop_back();
    }
    if (left < n) {
      current_combination.push_back('(');
      combinations(n, left + 1, right);
      current_combination.pop_back();
    }
  }
};

int main() {}
