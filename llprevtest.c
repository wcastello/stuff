#include <stdio.h>
#include <stdbool.h>

#include "linkedlist.h"

int main(int argc, char const *argv[])
{
    LinkedList list;
    LinkedList refs;
    list_init(&list, sizeof(int));
    list_init(&refs, sizeof(Node **));
    int data[10] = {1, 2, 3, 4};
    for (int i = 0; i < 4; ++i) {
        list_append(&list, &data[i]);
        list_append(&refs, &list.head);
    }

    Node *curr_ref = refs.head;

    list_remove_node(&list, *(Node **)curr_ref->data);
    list_pop(&refs);
    curr_ref = refs.head;

    list_remove_node(&list, *(Node **)curr_ref->data);
    list_pop(&refs);
    curr_ref = refs.head;

    list_remove_node(&list, *(Node **)curr_ref->data);
    list_pop(&refs);
    curr_ref = refs.head;


    list_remove_node(&list, *(Node **)curr_ref->data);
    list_pop(&refs);
    curr_ref = refs.head;

    list_int_print(&list);

    return 0;
}