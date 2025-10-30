#include "./DynamicArray/dynamicArray.c"
#include <stdio.h>

int main() {
  DynamicArray *da = init(4);
  append(5, da);
  append(3, da);
  append(2, da);
  for (int i = 0; i < da->size; i++) {
    printf("%d ", da->data[i]);
  }
  printf("\n");
  pop(da);
  pop(da);
  append(19, da);
  for (int i = 0; i < da->size; i++) {
    printf("%d ", da->data[i]);
  }
}
