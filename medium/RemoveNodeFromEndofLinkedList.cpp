#include <iostream>

using namespace std;
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *removeNthFromEnd(ListNode *head, int n) {

    ListNode dumy = ListNode(0);
    dumy.next = head;
    ListNode *f = &dumy, *m = head, *l = &dumy;
    int nth = n;

    while (nth > 0 and l->next != nullptr) {
      l = l->next;
      nth--;
    }
    while (l->next != nullptr) {
      f = f->next;
      m = m->next;
      l = l->next;
    }
    f->next = m->next;
    delete m;
    return dumy.next;
  }
};
