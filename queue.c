#include <stdlib.h>
#include <stdbool.h>
#include "linkedlist.h"
#include "queue.h"

void queue_init(Queue * q, size_t elemsize)
{
    q->data_list = malloc(sizeof(LinkedList));
    list_init(q->data_list, elemsize);
}

bool queue_enqueue(Queue *q, void * data)
{
    return list_append(q->data_list, data);
}

void * queue_dequeue(Queue *q)
{
    return list_pop_tail(q->data_list);
}

size_t queue_length(Queue *q)
{
    return q->data_list->length;
}