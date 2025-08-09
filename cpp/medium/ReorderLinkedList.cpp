
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  void reorderList(ListNode *head) {
    if (!head || !head->next)
      return;
    ListNode *mid = findMiddle(head);
    ListNode *temp = mid->next;
    mid->next = nullptr;
    ListNode *reversedMid = reverseList(temp);
    temp = head;
    ListNode *theAns = temp;
    while (temp and reversedMid) {
      ListNode *tempNext = temp->next;
      ListNode *revNext = reversedMid->next;
      temp->next = reversedMid;
      if (!tempNext)
        break;
      reversedMid->next = tempNext;
      temp = tempNext;
      reversedMid = revNext;
    }
  }

  ListNode *findMiddle(ListNode *head) {
    ListNode *f = head, *s = head;

    while (s and s->next) {
      f = f->next;
      s = s->next->next;
    }
    return f;
  }

  ListNode *reverseList(ListNode *head) {

    ListNode *f = nullptr, *s = head, *t = head->next;
    while (s) {
      t = s->next;
      s->next = f;
      f = s;
      s = t;
    }
    return f;
  }
};
