#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {

    unordered_map<int, int> mp;
    for (auto num : nums) {
      if (mp.find(num) == mp.end()) {
        mp.insert({num, 1});
      } else {
        mp[num]++;
      }
    }

    priority_queue<pair<int, int>> pq; // the default is min_heap
    for (auto pair : mp) {
      pq.push({-pair.second, pair.first});
      if (pq.size() > k) {
        pq.pop();
      }
    }
    vector<int> ans;
    while (!pq.empty()) {
      ans.push_back(pq.top().second);
      pq.pop();
    }
    return ans;
  }
};

int main() {}
