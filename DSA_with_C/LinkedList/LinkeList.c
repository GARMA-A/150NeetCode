#include <stdio.h>
#include <stdlib.h>

struct LinkedListNode {
  int data;
  struct LinkedListNode *next;
};

struct LinkedListNode *createNode(int data) {
  struct LinkedListNode *newNode =
      (struct LinkedListNode *)malloc(sizeof(struct LinkedListNode));
  newNode->data = data;
  newNode->next = NULL;
  return newNode;
}

struct LinkedListNode *append(struct LinkedListNode *head, int data) {
  if (head == NULL) {
    return createNode(data);
  }
  struct LinkedListNode *newNode =
      (struct LinkedListNode *)malloc(sizeof(struct LinkedListNode));
  newNode->data = data;
  newNode->next = NULL;
  struct LinkedListNode *current = head;
  while (current->next != NULL) {
    current = current->next;
  }
  current->next = newNode;
  return NULL;
}

struct LinkedListNode *appendleft(struct LinkedListNode *head, int data) {
  if (head == NULL) {
    return createNode(data);
  }
  struct LinkedListNode *newNode =
      (struct LinkedListNode *)malloc(sizeof(struct LinkedListNode));
  newNode->data = data;
  newNode->next = head;
  head = newNode;
  return NULL;
}

void display(struct LinkedListNode *head) {
  struct LinkedListNode *current = head;
  while (current != NULL) {
    printf("%d -> ", current->data);
    current = current->next;
  }
  printf("NULL\n");
}

void pop(struct LinkedListNode *head) {
  if (head == NULL) {
    return;
  }
  if (head->next == NULL) {
    free(head);
    head = NULL;
    return;
  }
  struct LinkedListNode *current = head;
  while (current->next->next != NULL) {
    current = current->next;
  }
  free(current->next);
  current->next = NULL;
}

void popleft(struct LinkedListNode **head) {
  if (*head == NULL) {
    return;
  }
  struct LinkedListNode *temp = *head;
  *head = (*head)->next;
  free(temp);
}

void freeList(struct LinkedListNode *head) {
  struct LinkedListNode *current = head;
  struct LinkedListNode *next;

  while (current != NULL) {
    next = current->next;
    free(current);
    current = next;
  }
}
