
#include <vector>
class Solution {
public:
  int missingNumber(std::vector<int> &nums) {
    int ans = (nums.size() * (nums.size() + 1)) / 2;

    for (auto num : nums) {
      ans -= num;
    }
    return ans;
  }
};
