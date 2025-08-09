#include <climits>
#include <iostream>
#include <stack>

using namespace std;

class MinStack {
  stack<long long> st;
  stack<long long> curmin;

public:
  MinStack() {}

  void push(int val) {
    if (curmin.empty() or val <= curmin.top()) {
      curmin.push(val);
    } else {
      curmin.push(curmin.top());
    }
    st.push(val);
  }

  void pop() {
    curmin.pop();
    st.pop();
  }

  int top() { return st.top(); }

  int getMin() { return curmin.top(); }
};
