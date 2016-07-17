#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdbool.h>

typedef struct Node {
    void *data;
    struct Node *next;
    struct Node *prev;
} Node;

typedef struct LinkedList {
    size_t elemsize;
    size_t length;
    Node *head;
    Node *tail;
} LinkedList;

void list_init(LinkedList * list, size_t elemsize);
bool list_append(LinkedList * list, void * data);
bool list_append_tail(LinkedList * list, void *data);
void list_remove_node(LinkedList * list, Node * node);
void list_remove(LinkedList * list, void * data);
void * list_pop(LinkedList *list);
void * list_pop_tail(LinkedList *list);
void list_int_print(LinkedList * list);
void list_in_place_merge(LinkedList *list_a, LinkedList *list_b);

#endif
