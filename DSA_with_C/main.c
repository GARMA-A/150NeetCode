#include <stdio.h>
#include <stdlib.h>

char *readString() {
  char *str = NULL;
  int size = 0;
  int capacity = 10;
  str = (char *)malloc(capacity * sizeof(char));
  if (str == NULL) {
    printf("memory allocation failed");
    exit(1);
  }
  char ch;
  while ((ch = getchar()) != '\n' && ch != EOF) {
    if (size == capacity - 1) {
      capacity *= 2;
      str = (char *)realloc(str, capacity * sizeof(char));
      if (str == NULL) {
        printf("memory allocation failed");
        exit(1);
      }
    }
    str[size++] = ch;
  }
  str[size] = '\0';
  return str;
}

int main() {
  char *str = readString();
  printf("this is the str %s", str);
  free(str);
}
