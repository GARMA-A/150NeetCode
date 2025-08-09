#include <unordered_map>
#include <vector>

using namespace std;

class Solution { // space :O(n) //

  vector<vector<int>> ans;
  unordered_map<int, bool> vistied;

public:
  vector<vector<int>> permute(vector<int> &nums) {
    vector<int> cur;
    helper(nums, cur);
    return ans;
  }

  void helper(vector<int> &nums, vector<int> &curPer) {
    if (curPer.size() == nums.size()) {
      this->ans.push_back(curPer);
      return;
    }
    for (int i = 0; i < nums.size(); i++) {
      if (not vistied[nums[i]]) {
        curPer.push_back(nums[i]);
        vistied[nums[i]] = true;
        helper(nums, curPer);
        curPer.pop_back();
        vistied[nums[i]] = false;
      }
    }
  }
};
