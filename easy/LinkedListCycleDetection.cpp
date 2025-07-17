#include <iostream>
#include <unordered_map>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {

  bool hasCycle(ListNode *head) {
    if (!head)
      return false;

    unordered_map<ListNode *, bool> visted;
    visted[head] = true;
    ListNode *temp = head->next;
    while (temp) {
      if (visted[temp]) {
        return true;
      } else {
        visted[temp] = true;
      }
    }
    return false;
  }
};

int main() {}
