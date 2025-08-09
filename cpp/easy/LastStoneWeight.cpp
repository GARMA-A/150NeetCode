#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
  priority_queue<int> mxheap;

public:
  int lastStoneWeight(vector<int> &stones) {
    for (auto stone : stones) {
      mxheap.push(stone);
    }
    while (mxheap.size() > 1) {
      int s1 = mxheap.top();
      mxheap.pop();
      int s2 = mxheap.top();
      mxheap.pop();
      mxheap.push(abs(s1 - s2));
    }
    return mxheap.top();
  }
};

int main() {}
