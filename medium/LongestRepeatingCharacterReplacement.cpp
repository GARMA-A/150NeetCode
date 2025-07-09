#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
  int characterReplacement(string s, int k) {
    int l = 0, mx_length = 0;
    int arr[26] = {0};
    for (int r = 0; r < s.length(); r++) {
      // we will need to see if the current window is valid or not
      // so i will check if (cur_window_len - most freq char)<=k
      arr[s[r] - 'A']++;
      int most_freq_char = max(most_freq_char, arr[s[r] - 'A']);
      int current_window_length = (r - l) + 1;
      while ((current_window_length - most_freq_char) > k) {
        arr[s[l] - 'A']--;
        l++;
      }
      mx_length = max(mx_length, current_window_length);
    }
    return mx_length;
  }
};
int main() {}
