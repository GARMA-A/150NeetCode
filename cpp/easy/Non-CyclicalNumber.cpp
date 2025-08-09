#include <iostream>

using namespace std;

class Solution {
public:
  bool isHappy(int n) {
    int slow = n, fast = sumOfSquares(n);
    while (slow != fast) {
      fast = sumOfSquares(fast);
      fast = sumOfSquares(fast);
      slow = sumOfSquares(slow);
    }
    return fast == 1;
  }

  int sumOfSquares(int n) {
    int sum = 0;
    while (n > 0) {
      sum += (n % 10) * (n % 10);
      n /= 10;
    }
    return sum;
  }
};

int main() {
  Solution s = Solution();
  cout << s.sumOfSquares(123);
}
