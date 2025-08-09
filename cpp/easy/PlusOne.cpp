#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
  vector<int> plusOne(vector<int> &digits) {
    deque<int> dq;
    // Input: digits = [1,2,3,4]
    //
    // Output: [1,2,3,5]
    int count = 1;
    for (int i = digits.size() - 1; i >= 0; i--) {
      int curNum = digits[i];
      if (curNum == 9 and count > 0) {
        curNum = 0;
        count = 1;
      } else {
        curNum += count;
        count = 0;
      }
      dq.push_front(curNum);
    }
    if (count > 0) {
      dq.push_front(count);
    }
    vector<int> ans(dq.begin(), dq.end());
    return ans;
  }
};
int main() {}
