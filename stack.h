#ifndef STACK_H
#define STACK_H

#include <stdbool.h>
#include "linkedlist.h"

typedef struct Stack {
    LinkedList *data_list;
    LinkedList *mins;
    size_t elemsize;
    int (*cmpfn)(const void *p, const void *q);
} Stack;

void stack_init(Stack *s, size_t elemsize, int (*cmpfn)(const void *p, const void *q));
void * stack_pop(Stack *s);
bool stack_push(Stack *s, void * data);
void * stack_peek(Stack *s);
bool stack_empty(Stack *s);
void * stack_min(Stack *s);
void stack_int_print(Stack *s);

#endif
