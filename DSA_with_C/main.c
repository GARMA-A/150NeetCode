#include "./LinkedList/LinkeList.c"

int main() {
  struct LinkedListNode *head =
      (struct LinkedListNode *)malloc(sizeof(struct LinkedListNode));
  head->data = -1;

  for (int i = 0; i < 5; i++) {
    append(head, i);
  }
  display(head);
  popleft(&head);
  display(head);
  pop(head);
  display(head);
}
