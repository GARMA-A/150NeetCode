#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
  vector<vector<int>> ans;

public:
  vector<vector<int>> subsetsWithDup(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    vector<int> subset;
    helper(nums, 0, subset);
    return ans;
  }

  void helper(vector<int> &nums, int index, vector<int> &subset) {
    ans.push_back(subset);
    for (int i = index; i < nums.size(); ++i) {
      if (i > index && nums[i] == nums[i - 1])
        continue;
      subset.push_back(nums[i]);
      helper(nums, i + 1, subset);
      subset.pop_back();
    }
  }
};

int main() {}
