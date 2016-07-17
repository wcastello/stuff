#ifndef QUEUE_H
#define QUEUE_H

#include "linkedlist.h"

typedef struct Queue {
    LinkedList *data_list;
    size_t elemsize;
} Queue;

void queue_init(Queue * q, size_t elemsize);
bool queue_enqueue(Queue *q, void * data);
void * queue_dequeue(Queue *q);
size_t queue_length(Queue *q);

#endif