#include <algorithm>
#include <charconv>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {

  vector<vector<int>> ans;
  unordered_map<int, int> count;

public:
  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {
    vector<int> cur;
    vector<int> A;
    for (int num : candidates) {
      if (!count[num]) {
        A.push_back(num);
      }
      count[num]++;
    }
    backtrack(A, target, 0, cur);
    return ans;
  }
  void backtrack(vector<int> &candidates, int target, int i, vector<int> &cur) {
    if (target == 0) {
      ans.push_back(cur);
      return;
    } else if (target < 0 || i >= candidates.size()) {
      return;
    }

    if (count[candidates[i]]) {
      cur.push_back(candidates[i]);
      count[candidates[i]]--;
      backtrack(candidates, target - candidates[i], i, cur);
      cur.pop_back();
      count[candidates[i]]++;
    }
    backtrack(candidates, target, i + 1, cur);
  }
};

int main() {}
