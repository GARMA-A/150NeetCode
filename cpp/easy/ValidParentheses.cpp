#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
  bool isValid(string s) {
    if (s.size() & 1)
      return false;
    stack<char> st;
    for (auto ch : s) {
      if (ch == '(' || ch == '{' || ch == '[') {
        st.push(ch);
      } else {
        if (st.empty())
          return false;
        char top = st.top();
        if ((ch == ')' && top != '(') || (ch == '}' && top != '{') ||
            (ch == ']' && top != '[')) {
          return false;
        }
        st.pop();
      }
    }
    if (st.empty())
      return true;
    else
      return false;
  }
};
