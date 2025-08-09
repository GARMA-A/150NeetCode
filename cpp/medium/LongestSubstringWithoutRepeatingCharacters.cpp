#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {

public:
  int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> mp;
    int l = 0, r = 0;
    int mx_length = 0;
    while (r < s.length()) {
      if (mp.find(s[r]) != mp.end() && mp[s[r]] > 0) {
        mp[s[l]]--;
        l++;
      } else {
        mp[s[r]]++;

        mx_length = max(mx_length, (r - l) + 1);
        r++;
      }
    }
    return mx_length;
  }
};

int main() {}
