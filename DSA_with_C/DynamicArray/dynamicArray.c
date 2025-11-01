#include "dyncmicArray.h"
#include <stdlib.h>
#include <string.h>

DynamicArray *init(int initialCapacity) {
  DynamicArray *da = (DynamicArray *)malloc(sizeof(DynamicArray));
  da->data = (char **)malloc(initialCapacity * sizeof(char *));
  da->size = 0;
  da->capacity = initialCapacity;
  return da;
}

void deinit(DynamicArray *da) {
  for (int i = 0; i < da->size; i++) {
    free(da->data[i]);
  }
  free(da->data);
  free(da);
}

void append(char *newValue, DynamicArray *da) {
  if (da->capacity == da->size) {
    da->capacity *= 2;
    da->data[da->size] = (char *)malloc(strlen(newValue) + 1);
    strcpy(da->data[da->size], newValue);
  }
  da->data[da->size++] = newValue;
}

void pop(DynamicArray *da) { da->data[--da->size] = NULL; }

char *top(DynamicArray *da) {
  if (da->size > 0) {
    return da->data[da->size - 1];
  }
  return NULL;
}
