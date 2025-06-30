#include <unordered_set>
#include <vector>

using namespace std;
class Solution {
public:
  int longestConsecutive(vector<int> &nums) {
    unordered_set<int> st;
    for (int num : nums) { // o(n)
      st.insert(num);
    }
    int final_answer = 0;
    for (auto num : nums) {
      int count = 0;
      int currentNum = num;
      while (st.find(currentNum) != st.end()) {
        count++;
        currentNum++;
      }
      final_answer = max(count, final_answer);
    }
    return final_answer;
  }
};
