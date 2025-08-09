
#include <vector>

using namespace std;
class Solution {
public:
  vector<vector<int>> ans;
  vector<vector<int>> combinationSum(vector<int> &nums, int target) {
    vector<int> cur;
    helper(nums, cur, target, 0);
    return ans;
  }

  void helper(vector<int> &nums, vector<int> &cur, int target, int i) {
    if (target < 0 || i >= nums.size())
      return;

    if (target == 0) {
      ans.push_back(cur);
      return;
    }

    cur.push_back(nums[i]);
    helper(nums, cur, target - nums[i], i);
    cur.pop_back();
    helper(nums, cur, target, i + 1);
  }
};
