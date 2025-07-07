#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int search(vector<int> &nums, int target) {
    //    /7
    //   /6
    //  /5
    //-/4------------
    //        /4
    //       /3
    //      /2
    //     /1
    // [4,5,6,7,1,2,3,4] any rotated sorted array will be like this

    int l = 0, r = nums.size() - 1;
    while (l <= r) {
      int mid = l + (r - l) / 2;
      if (nums[mid] == target)
        return mid;

      if (nums[mid] >= nums[l]) { // we are in the left side now
        if (target > nums[mid] or target < nums[l]) {
          l = mid + 1;
        } else {
          r = mid - 1;
        }

      } else { // we are on the right side now
        if (target < nums[mid] or target > nums[r]) {
          r = mid - 1;
        } else {
          l = mid + 1;
        }
      }
    }
    return -1;
  }
};
