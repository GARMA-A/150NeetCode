#include <algorithm>
#include <cstddef>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxArea(vector<int> &heights) {
    size_t size = heights.size();
    int l = 0, r = size - 1;
    int mx_area = 0;
    while (l < r) {
      int area = (r - l) * min(heights[l], heights[r]);
      if (heights[l] <= heights[r]) {
        l++;
      } else {
        r--;
      }
      mx_area = max(mx_area, area);
    }
    return mx_area;
  }
};

int main() {
  Solution *s = new Solution;
  vector<int> v = {1, 7, 2, 5, 4, 7, 3, 6};
  cout << s->maxArea(v);
}
