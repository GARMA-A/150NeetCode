#include <cstddef>
#include <iostream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> dailyTemperatures(vector<int> &temperatures) {
    size_t size = temperatures.size();
    stack<pair<int, int>> st;
    vector<int> result(size);
    for (int i = 0; i < size; i++) {
      while (!st.empty() && temperatures[i] > temperatures[st.top().second]) {
        result[st.top().second] = i - st.top().second;
        st.pop();
      }
      st.push({temperatures[i], i});
    }

    pair<int, int> top;
    if (not st.empty()) {
      top = st.top();
      st.pop();
    }
    while (not st.empty()) {
      if (not st.empty() and top > st.top()) {
        result[st.top().second] = top.second - st.top().second;
      } else if (not st.empty()) {
        top = st.top();
      }
      st.pop();
    }
    return result;
  }
};

int main() {
  vector<int> temperatures = {30, 38, 30, 36, 35, 40, 28};
  Solution *s = new Solution;

  vector<int> result = s->dailyTemperatures(temperatures);
  for (int el : result) {
    cout << el << " ";
  }
}
