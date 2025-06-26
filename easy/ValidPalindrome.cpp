#include <algorithm>
#include <cctype>
#include <iostream>

using namespace std;

class Solution {
public:
  bool isPalindrome(string s) {
    string filter;
    for (auto ch : s) {
      if (isalnum(ch)) {
        filter += tolower(ch);
      }
    }

    string reversed = filter;
    reverse(reversed.begin(), reversed.end());
    return reversed == filter;
  }
};

int main() {

  string str = "fr AM Arf";
  Solution *s = new Solution();
  cout << s->isPalindrome(str) << "yes";
}
