#ifndef STACKSET_H
#define STACKSET_H

#include <stdbool.h>
#include "stack.h"
#include "linkedlist.h"

typedef struct StackSet {
    Stack **stacks;
    size_t elemsize;
    size_t curr_stack;
    unsigned int threshold;
} StackSet;

void stackset_init(StackSet *s, size_t elemsize, unsigned int threshold);
void * stackset_pop(StackSet *s);
bool stackset_push(StackSet *s, void * data);
void * stackset_peek(StackSet *s);
bool stackset_empty(StackSet *s);
void stackset_int_print(StackSet *s);

#endif