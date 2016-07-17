#include <stdlib.h>
#include <stdbool.h>

#include "stack.h"
#include "linkedlist.h"

void stack_init(Stack *s, size_t elemsize, int (*cmpfn)(const void *p, const void *q))
{
    s->elemsize = elemsize;
    s->cmpfn = cmpfn;
    s->data_list = malloc(sizeof(LinkedList));
    s->mins = malloc(sizeof(LinkedList));

    list_init(s->data_list, elemsize);
    list_init(s->mins, elemsize);
}

// void stack_free(Stack *s)
// {
//     // should use special freefn if data is complex, then call freelist

// }

void * stack_pop(Stack *s)
{
    void *data = list_pop(s->data_list);
    if (s->cmpfn && s->mins->length > 0 && s->cmpfn(data, s->mins->head->data) == 0) {
        list_pop(s->mins);
    }
    return data;
}

bool stack_push(Stack *s, void * data)
{
    if (list_append(s->data_list, data)) {
        if (s->cmpfn) {
            if (s->mins->length == 0)
                list_append(s->mins, data);
            else if (s->cmpfn(data, s->mins->head->data) <= 0) {
                list_append(s->mins, data);
            }
            return true;
        }
        return true;
    }
    return false;
}

void * stack_peek(Stack *s)
{
    if (s->data_list->length > 0)
        return s->data_list->head->data;
    return NULL;
}

bool stack_empty(Stack *s)
{
    if (s->data_list->length == 0)
        return true;

    return false;
}

void * stack_min(Stack *s)
{
    if (s->mins->length > 0)
        return s->mins->head->data;
    return NULL;
}

void stack_int_print(Stack *s)
{
    list_int_print(s->data_list);
}