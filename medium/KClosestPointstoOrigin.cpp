#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct triple {
  int length;
  int x;
  int y;

  bool operator<(const triple &other) const { return length < other.length; }
};

class Solution {

  priority_queue<triple> mxheap;

public:
  vector<vector<int>> kClosest(vector<vector<int>> &points, int k) {
    for (auto pair : points) {
      int length = pair[0] * pair[0] + pair[1] * pair[1];
      mxheap.push({length, pair[0], pair[1]});
      if (mxheap.size() > k) {
        mxheap.pop();
      }
    }
    vector<vector<int>> ans;
    while (!mxheap.empty()) {
      ans.push_back({mxheap.top().x, mxheap.top().y});
      mxheap.pop();
    }
    return ans;
  }
};

int main() {}
