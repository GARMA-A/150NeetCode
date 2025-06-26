#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  bool hasDuplicate(vector<int> &nums) {
    return unordered_set<int>(nums.begin(), nums.end()).size() < nums.size();
  }
};

int main() {}
