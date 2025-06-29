#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  string encode(vector<string> &strs) {
    string ans;
    for (string str : strs) {
      int size = str.size();
      string sizeStr = to_string(size) + '#' + str;
      ans += sizeStr;
    }
    return ans;
  }

  vector<string> decode(string s) {
    vector<string> ans;
    int i = 0;
    while (i < s.size()) {
      string next_word_chars_count = "";
      while (s[i] != '#') {
        next_word_chars_count += s[i];
        i++;
      }
      int word_size = stoi(next_word_chars_count);
      i++;
      string current_word = "";
      while (word_size > 0) {
        current_word += s[i];
        i++;
        word_size--;
      }
      ans.push_back(current_word);
    }
    return ans;
  }
};

int main() {}
