#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int minEatingSpeed(vector<int> &piles, int h) {
    int r = *max_element(piles.begin(), piles.end()), l = 1;
    int res = r;
    while (l < r) {
      int k = l + (r - l) / 2;
      int hours_needed = 0;
      for (auto p : piles) {
        hours_needed += ceil(static_cast<double>(p) / k);
      }
      if (hours_needed > h) {
        l = k + 1;
      } else {
        res = k;
        r = k - 1;
      }
    }
    return res;
  }
};

int main() {}
