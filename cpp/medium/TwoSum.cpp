#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {

    unordered_map<int, int> mp;

    for (int i = 0; i < nums.size(); i++) {
      int ans = target - nums[i];
      if (mp.find(ans) != mp.end()) {
        return {mp[ans], i};
      }
      mp.insert({nums[i], i});
    }
    return {-1, -1};
  }
};
