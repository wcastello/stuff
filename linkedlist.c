#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "linkedlist.h"

void list_init(LinkedList * list, size_t elemsize)
{
    list->head = NULL;
    list->tail = NULL;
    list->elemsize = elemsize;
    list->length = 0;
}

bool list_append(LinkedList * list, void * data)
{
    if (!list->head) {
        list->head = malloc(sizeof(Node));
        list->tail = list->head;
        list->head->data = malloc(list->elemsize);
        memcpy(list->head->data, data, list->elemsize);
        list->head->next = NULL;
        list->head->prev = NULL;
    } else {
        Node *n = malloc(sizeof(Node));
        n->data = malloc(list->elemsize);
        memcpy(n->data, data, list->elemsize);
        n->next = list->head;
        list->head->prev = n;
        n->prev = NULL;
        list->head = n;
    }
    list->length++;

    return true;
}

bool list_append_tail(LinkedList * list, void *data)
{
    if (!list->head) {
        list->head = malloc(sizeof(Node));
        list->tail = list->head;
        list->head->data = malloc(list->elemsize);
        memcpy(list->head->data, data, list->elemsize);
        list->head->next = NULL;
    } else {
        Node *n = malloc(sizeof(Node));
        n->next = NULL;
        n->data = malloc(list->elemsize);
        memcpy(n->data, data, list->elemsize);
        list->tail->next = n;
        n->prev = list->tail;
        list->tail = n;
    }
    list->length++;

    return true;
}

void list_remove_node(LinkedList * list, Node * node) {
    if (node->prev && node->next) { // middle, list length >= 3
        node->prev->next = node->next;
    } else if (node->prev && !node->next) { // tail, list length >= 2
        list_pop_tail(list);
        // node->prev->next = NULL;
        // list->tail = node->prev;
    } else if (!node->prev && node->next) { // head, list length >= 2
        list_pop(list);
        // node->next->prev = NULL;
        // node->head = node->next;
    } else { // head == tail, list length == 1
        list_pop(list);
    }
    // there's got to be some free function for the node content too or we'll leak memory
}

void * list_pop(LinkedList *list)
{
    void *data = NULL;
    if (list->length > 0) {
        data = list->head->data;
        Node *to_pop = list->head;
        list->head = list->head->next;
        free(to_pop);
        list->length--;
        if (list->length == 0)
            list->tail = NULL;
        else {
            list->head->prev = NULL;
        }
    }
    return data;
}

void * list_pop_tail(LinkedList *list)
{
    void *data = NULL;
    if (list->length > 0) {
        data = list->tail->data;
        Node *to_pop = list->tail;
        list->tail = list->tail->prev;
        free(to_pop);
        list->length--;
        if (list->length == 0) {
            list->head = list->tail;
        }
        else
            list->tail->next = NULL;
    }
    return data;
}


void list_int_print(LinkedList * list)
{
    Node *curr = list->head;
    printf("[");
    while (curr) {
        if (curr->next)
            printf("%d, ", *(int *)curr->data);
        else
            printf("%d", *(int *)curr->data);
        curr = curr->next;
    }
    printf("]\n");
}

void list_in_place_merge(LinkedList *list_a, LinkedList *list_b)
{
    list_a->tail->next = list_b->head;
    list_a->tail = list_b->tail;
}
