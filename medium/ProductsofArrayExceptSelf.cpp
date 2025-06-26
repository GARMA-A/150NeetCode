#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> productExceptSelf(vector<int> &nums) {
    int size = nums.size(), mult = 1;
    vector<int> prev(size), cur(size), ans(size);

    for (int i = 0; i < size; i++) {
      mult *= nums[i];
      prev[i] = mult;
    }
    mult = 1;

    for (int i = size - 1; i > 0; i--) {
      mult *= nums[i];
      cur[i] = mult;
    }
    mult = 1;

    ans[0] = cur[1];
    ans[size - 1] = prev[size - 2];

    int prevPointer = 0, curPointer = 2, anspointer = 1;

    while (curPointer < size) {
      ans[anspointer] = prev[prevPointer] * cur[curPointer];

      prevPointer++;
      curPointer++;
      anspointer++;
    }

    return ans;
  }
};

int main() {
  Solution *s1 = new Solution();
  vector<int> arr = {1, 2, 4, 6}, ans;
  ans = s1->productExceptSelf(arr);

  for (int i = 0; i < ans.size(); i++)
    cout << ans[i] << " ";
}
