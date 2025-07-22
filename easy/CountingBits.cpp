#include <unordered_map>
#include <vector>
class Solution {
public:
  std::vector<int> countBits(int n) {
    std::vector<int> ans;
    int arr[1000] = {-1};
    if (n == 0) {
      return {0};
    }

    arr[0] = 0;
    ans.push_back(arr[0]);
    if (n > 0) {
      arr[1] = 1;
      ans.push_back(arr[2]);
    }
    if (n > 1) {
      arr[2] = 1;
      ans.push_back(arr[2]);
    }
    if (n > 2) {
      arr[3] = 2;
      ans.push_back(arr[3]);
    }
    if (n > 3)
      for (int i = 4; i < n; i++) {
        arr[i] = arr[i - 4] + 1;
        ans.push_back(arr[i]);
      }
    return ans;
  }
};
