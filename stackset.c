#include <stdio.h>
#include <stdlib.h>
#include "stackset.h"
#include "stack.h"

void stackset_init(StackSet *s, size_t elemsize, unsigned int threshold)
{
    s->curr_stack = 0;
    s->elemsize = elemsize;
    s->threshold = threshold;
    s->stacks = malloc(sizeof(Stack *));
    s->stacks[0] = malloc(sizeof(Stack));
    stack_init(s->stacks[0], elemsize, NULL);
}

void * stackset_pop(StackSet *s)
{
    if (s->curr_stack > 0 && stack_empty(s->stacks[s->curr_stack]))
        s->curr_stack--;
    return stack_pop(s->stacks[s->curr_stack]);
}

bool stackset_push(StackSet *s, void * data)
{
    bool merge = false;
    if (s->stacks[s->curr_stack]->data_list->length >= s->threshold) {
        s->curr_stack++;
        s->stacks = realloc(s->stacks, (s->curr_stack+1)*sizeof(Stack *));
        s->stacks[s->curr_stack] = malloc(sizeof(Stack));
        stack_init(s->stacks[s->curr_stack], s->elemsize, NULL);
        merge = true;
    }
    if (stack_push(s->stacks[s->curr_stack], data))
        if (merge)
            list_in_place_merge(s->stacks[s->curr_stack]->data_list, s->stacks[s->curr_stack-1]->data_list);
        return true;
    return false;
}

void * stackset_peek(StackSet *s)
{
    if (s->curr_stack > 0 && stack_empty(s->stacks[s->curr_stack]))
        s->curr_stack--;
    return stack_peek(s->stacks[s->curr_stack]);
}

bool stackset_empty(StackSet *s)
{
    return (s->curr_stack == 0) &&
        stack_empty(s->stacks[s->curr_stack]);
}

void stackset_int_print(StackSet *s)
{
    list_int_print(s->stacks[s->curr_stack]->data_list);
}