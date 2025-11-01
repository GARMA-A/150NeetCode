#ifndef DYNAMIC_STRING_ARRAY_H
#define DYNAMIC_STRING_ARRAY_H

// --- Type Definition ---
// 'data' is now a 'char**' (a pointer to an array of 'char*' pointers)
typedef struct {
  char **data;
  int size;
  int capacity;
} DynamicArray;

// --- Function Prototypes ---
// Note the changes in function parameters and return types

/**
 * @brief Initializes a new DynamicArray for strings.
 * @param initialCapacity The starting capacity (number of strings).
 * @return A pointer to the newly allocated DynamicArray.
 */
DynamicArray *init(int initialCapacity);

/**
 * @brief Frees all memory associated with the DynamicArray,
 * including all individual strings stored within it.
 * @param da A pointer to the DynamicArray to be deallocated.
 */
void deinit(DynamicArray *da);

/**
 * @brief Appends a *copy* of a string to the end of the array.
 * @param newValue The null-terminated string to append.
 * @param da A pointer to the DynamicArray.
 */
void append(char *newValue, DynamicArray *da);

/**
 * @brief Removes the last string from the array and frees its memory.
 * @param da A pointer to the DynamicArray.
 */
void pop(DynamicArray *da);

/**
 * @brief Returns a pointer to the last string in the array without removing it.
 * @param da A pointer to the DynamicArray.
 * @return A pointer to the last string, or NULL if the array is empty.
 */
char *top(DynamicArray *da);

/**
 * @brief Gets the string at a specific index.
 * @param index The index to retrieve.
 * @param da A pointer to the DynamicArray.
 *s * @return A pointer to the string, or NULL if the index is out of bounds.
 */
char *getAt(int index, DynamicArray *da);

/**
 * @brief Replaces the string at a specific index with a *copy* of newValue.
 * @param index The index to set. Must be within the current size.
 * @param newValue The new string value.
 * @param da A pointer to the DynamicArray.
 */
void setAt(int index, char *newValue, DynamicArray *da);

#endif // DYNAMIC_STRING_ARRAY_H
