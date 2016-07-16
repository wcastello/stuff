#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct LinkedList {
    Node *head;
} LinkedList;


void list_init(LinkedList * list);
void list_append(LinkedList * list, Node * node);
void list_print(LinkedList * list);
bool node_del_middle(Node * n);
LinkedList * list_partition(LinkedList * list, Node * node);

int main(int argc, char const *argv[])
{
    LinkedList list;
    list_init(&list);

    Node n1, n2, n3, n4, n5, n6, n7, n8, n9;
    n1.data = 1;
    n2.data = 2;
    n3.data = -3;
    n4.data = 5;
    n5.data = 3;
    n6.data = 4;
    n7.data = 32;
    n8.data = -1;
    n9.data = -5;
    list_append(&list, &n1);
    list_append(&list, &n2);
    list_append(&list, &n3);
    list_append(&list, &n4);
    list_append(&list, &n5);
    list_append(&list, &n6);
    list_append(&list, &n7);
    list_append(&list, &n8);
    list_append(&list, &n9);

    list_print(&list);

    printf("Partitioning around value %d\n", n5.data);
    LinkedList *p = list_partition(&list, &n5);
    // node_del_middle(&n3);
    list_print(p);

    return 0;
}

void list_init(LinkedList * list)
{
    list->head = NULL;
}


void list_append(LinkedList * list, Node * node)
{
    node->next = list->head;
    list->head = node;
}

void list_print(LinkedList * list)
{
    Node *curr = list->head;
    printf("[");
    while (curr) {
        if (curr->next)
            printf("%d, ", curr->data);
        else
            printf("%d]\n", curr->data);
        curr = curr->next;
    }
}

bool node_del_middle(Node * n)
{
    if (!n || !n->next)
        return false;

    Node *tmp = n->next;
    n->data = n->next->data;
    n->next = n->next->next;
    return true;
}

LinkedList * list_partition(LinkedList * list, Node * node)
{
    LinkedList *left, *right;
    Node *curr, *left_tail;

    left = malloc(sizeof(LinkedList));
    right = malloc(sizeof(LinkedList));

    list_init(left);
    list_init(right);

    curr = list->head;
    left_tail = NULL;

    while (curr) {
        Node *n = malloc(sizeof(Node));
        n->data = curr->data;
        if (curr->data < node->data) {
            if (!left->head)
                left_tail = n;
            list_append(left, n);
        } else {
            list_append(right, n);
        }
        curr = curr->next;
    }

    list_print(left);
    list_print(right);

    if (left_tail) {
        left_tail->next = right->head;
        free(right);
    } else {
        free(left);
        left = right;
    }

    return left;
}
