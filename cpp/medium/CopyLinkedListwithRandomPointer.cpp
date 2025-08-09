#include <iostream>
#include <unordered_map>

using namespace std;

class Node {
public:
  int val;
  Node *next;
  Node *random;

  Node(int _val) {
    val = _val;
    next = NULL;
    random = NULL;
  }
};

class Solution {
public:
  Node *copyRandomList(Node *head) {
    unordered_map<Node *, Node *> mp;
    Node *temp = head;
    while (temp) {
      Node *newNode = new Node(temp->val);
      mp.insert({temp, newNode});
      temp = temp->next;
    }
    temp = head;
    while (temp) {
      Node *copy = mp[temp];
      copy->next = mp[temp->next];
      copy->random = mp[temp->random];
      temp = temp->next;
    }
    return mp[head];
  }
};

int main() {}
