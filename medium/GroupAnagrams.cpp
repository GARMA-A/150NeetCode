#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    unordered_map<string, vector<string>> mp;

    int freq[26] = {0};
    for (int i = 0; i < strs.size(); i++) {
      for (auto ch : strs[i])
        freq[ch - 'a']++;

      string key = "";
      for (int i = 0; i < 26; i++) {
        while (freq[i] > 0) {
          key += i + 'a';
          freq[i]--;
        }
      }
      if (mp.find(key) != mp.end()) {
        mp[key].push_back(strs[i]);
      } else {
        mp.insert({key, {strs[i]}});
      }
    }

    vector<vector<string>> ans;
    for (auto pair : mp) {
      ans.push_back(pair.second);
    }
    return ans;
  }
};
