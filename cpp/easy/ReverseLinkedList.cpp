#include <iostream>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

using namespace std;

class Solution {
public:
  ListNode *reverseList(ListNode *head) {
    if (head == nullptr)
      return head;
    ListNode *first = nullptr, *second = head, *third = head->next;
    while (second) {
      third = second->next;
      second->next = first;
      first = second;
      second = third;
    }
    return first;
  }
};

int main() {}
