#include <charconv>
#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

class Solution {
  stack<int> st;
  int ans = 0;

public:
  int evalRPN(vector<string> &tokens) {
    for (int i = 0; i < tokens.size(); i++) {
      if (tokens[i] == "+" and not st.empty()) {
        int first = st.top(), second;
        st.pop();
        if (st.empty()) {
          continue;
        }
        second = st.top();
        st.pop();
        this->ans += (first + second);
      } else if (tokens[i] == "-" and not st.empty()) {
        int first = st.top(), second;
        st.pop();
        if (st.empty()) {
          continue;
        }
        second = st.top();
        st.pop();
        this->ans += (first - second);
      } else if (tokens[i] == "/" and not st.empty()) {
        int first = st.top(), second;
        st.pop();
        if (st.empty()) {
          continue;
        }
        second = st.top();
        st.pop();
        this->ans += (first / second);
      } else if (tokens[i] == "*" and not st.empty()) {
        int first = st.top(), second;
        st.pop();
        if (st.empty()) {
          continue;
        }
        second = st.top();
        st.pop();
        this->ans += (first * second);
      } else {
        st.push(stoi(tokens[i]));
      }
    }
    return this->ans;
  }
};

int main() {}
