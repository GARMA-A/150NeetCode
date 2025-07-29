#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
  priority_queue<int, vector<int>, greater<int>> minHeap;

public:
  int findKthLargest(vector<int> &nums, int k) {
    for (auto num : nums) {
      minHeap.push(num);
      if (minHeap.size() > k) {
        minHeap.pop();
      }
    }
    return minHeap.top();
  }
};

int main() {
  Solution s = Solution();
  vector<int> nums = {2, 3, 1, 1, 5, 5, 4};
  cout << s.findKthLargest(nums, 3);
}
