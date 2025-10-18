#include <bits/posix2_lim.h>
#include <stdio.h>
#include <stdlib.h>

struct Queue {
  int *data;
  int front;
  int rear;
  int capacity;
  int size;
};

void initQueue(struct Queue *q, int capacity) {
  q->capacity = capacity;
  q->front = 0;
  q->rear = -1;
  q->size = 0;
  q->data = (int *)malloc(capacity * sizeof(int));
}

int isFull(struct Queue *q) { return q->size == q->capacity; }

int isEmpty(struct Queue *q) { return q->size == 0; }

void enqueue(struct Queue *q, int value) {
  if (isFull(q)) {
    printf("Queue is full\n");
    return;
  }
  q->rear = (q->rear + 1) % q->capacity;
  q->data[q->rear] = value;
  q->size++;
}

void dequeue(struct Queue *q) {
  if (isEmpty(q)) {
    printf("Queue is empty\n");
    return;
  }
  q->front = (q->front + 1) % q->capacity;
  q->size--;
}
