#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
  vector<vector<int>> threeSum(vector<int> &nums) {
    vector<vector<int>> ans;
    int size = nums.size();
    sort(nums.begin(), nums.end());

    for (int i = 0; i < size; i++) {
      if (nums[i] > 0)
        break;
      if (i > 0 && nums[i] == nums[i - 1])
        continue;
      int a = nums[i];
      int l = i + 1, r = size - 1;
      while (l < r) {
        if (nums[l] + nums[r] + a == 0) {
          ans.push_back({a, nums[l], nums[r]});
          l++;
          r--;
          while (l < r && nums[l] == nums[l - 1]) {
            l++;
          }
        } else if ((nums[l] + nums[r] + a) > 0) {
          r--;
        } else {
          l++;
        }
      }
    }
    return ans;
  }
};
