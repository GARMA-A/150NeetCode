#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
  bool checkInclusion(string s1, string s2) {
    if (s1.size() > s2.size())
      return false;
    int counts1[26] = {0}, counts2[26] = {0};
    for (int i = 0; i < s1.size(); i++) {
      counts1[s1[i] - 'a']++;
      counts2[s2[i] - 'a']++;
    }
    int matches = 0;
    for (int i = 0; i < 26; i++) {
      if (counts1[i] == counts2[i])
        matches++;
    }
    int l = 0;
    for (int r = s1.size(); r < s2.size(); r++) {
      if (matches == 26)
        return true;
      int idxAdd = s2[r] - 'a';
      int idxRemove = s2[l] - 'a';
      counts2[idxAdd]++;
      if (counts2[idxAdd] == counts1[idxAdd])
        matches++;
      else if (counts2[idxAdd] - 1 == counts1[idxAdd])
        matches--;
      counts2[idxRemove]--;
      if (counts2[idxRemove] == counts1[idxRemove])
        matches++;
      else if (counts2[idxRemove] + 1 == counts1[idxRemove])
        matches--;
      l++;
    }
    return matches == 26;
  }
};
