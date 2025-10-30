#include <stdlib.h>
typedef struct {
  int *data;
  int size;
  int capacity;
} DynamicArray;

DynamicArray *init(int initialCapacity) {
  DynamicArray *da = (DynamicArray *)malloc(sizeof(DynamicArray));
  da->data = (int *)malloc(initialCapacity * sizeof(int));
  da->size = 0;
  da->capacity = initialCapacity;
  return da;
}

void append(int newValue, DynamicArray *da) {
  if (da->capacity == da->size) {
    da->capacity *= 2;
    da->data = realloc(da->data, sizeof(int) * da->capacity);
  }
  da->data[da->size++] = newValue;
}

void pop(DynamicArray *da) { da->data[--da->size] = -1; }

int top(DynamicArray *da) {
  if (da->size > 0) {
    return da->data[da->size - 1];
  }
  return -1; // or some other error value
}
