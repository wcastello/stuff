#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>

#include "linkedlist.h"
#include "stack.h"

typedef struct Graph {
    unsigned int n;
    int e;
    size_t length;
    size_t data_size;
    struct Vertex {
        void *data; // this needs a map from label to vertex
        LinkedList a;
    } *vertices;
} Graph;


void graph_init(Graph * g, unsigned int n, size_t data_size);
void graph_add_vertex(Graph * g, void * data);
void graph_add_edge(Graph * g, void * u, void * v);
void graph_del_edge(Graph *g, void * u, void * v);

#define IDX_LABEL(c) (c - 97)
void print_build_order(Graph * g);
void compute_in_degree(Graph * g, int in_degree[], int n);

int main(int argc, char const *argv[])
{
    Graph g;
    graph_init(&g, 10, sizeof(char));

    int n;
    printf("Enter number of projects: ");
    scanf("%d", &n);

    /* read projects */
    char project;
    printf("Enter a list of project labels: ");
    for (int i = 0; i < n; ++i) {
        scanf(" %c", &project);
        graph_add_vertex(&g, &project);
    }

    /* read dependencies */
    char a, b;
    printf("Enter dependencies in the form \"a b\" where project b depends on a, finish with a \". .\":\n");
    while (1) {
        scanf(" %c %c", &a, &b);
        if (a == '.' || b == '.')
            break;
        graph_add_edge(&g, &a, &b);
    }

    print_build_order(&g);

    return 0;
}

void print_build_order(Graph * g)
{
    // topological sorting
    Stack s;
    int in_degree[g->length];
    bool visited[g->length];

    for (int i = 0; i < g->length; ++i) {
        in_degree[i] = 0;
        visited[i] = false;
    }

    stack_init(&s, sizeof(struct Vertex *), NULL);
    compute_in_degree(g, in_degree, g->n);

    struct Vertex *p;
    for (int i = 0; i < g->length; ++i) {
        if (in_degree[i] == 0) {
            p = &g->vertices[i];
            stack_push(&s, &p);
        }
    }

    struct Vertex *v, *u;
    char v_idx_label, u_idx_label;
    Node *curr; // used to traverse adjacency list; // TODO: implement traverse on the list itself
    while (!stack_empty(&s)) {
        v = *(struct Vertex **)stack_pop(&s);
        v_idx_label = *(char *)v->data;
        if (!visited[IDX_LABEL(v_idx_label)]) {
            printf("%c ", v_idx_label);
            visited[IDX_LABEL(v_idx_label)] = true;
            curr = (v->a).head;
            while (curr) {
                u = *(struct Vertex **)curr->data;
                u_idx_label = *(char *)u->data;
                if (!visited[IDX_LABEL(u_idx_label)]) {
                    graph_del_edge(g, &v_idx_label, &u_idx_label);
                    in_degree[IDX_LABEL(u_idx_label)]--;
                    if (in_degree[IDX_LABEL(u_idx_label)] == 0) {
                        stack_push(&s, &u);
                    }
                }
                curr = curr->next;
            }
        }
    }
    assert(g->e == 0);
}

void compute_in_degree(Graph * g, int in_degree[], int n)
{
    Node *curr;
    struct Vertex *v, *u;
    char v_idx_label, u_idx_label;

    for (int i = 0; i < g->length; ++i) {
        v = &g->vertices[i];
        v_idx_label = *(char *)v->data;
        curr = (v->a).head;

        while (curr) {
            u = *(struct Vertex **)curr->data;
            u_idx_label = *(char *)u->data;
            in_degree[IDX_LABEL(u_idx_label)]++;
            curr = curr->next;
        }
    }
}

void graph_init(Graph * g, unsigned int n, size_t data_size)
{
    g->n = n;
    g->length = 0;
    g->e = 0;
    g->data_size = data_size;
    g->vertices = malloc(n * sizeof(struct Vertex));

    for (int i = 0; i < n; ++i) {
        g->vertices[i].data = NULL;
        list_init(&g->vertices[i].a, sizeof(struct Vertex *));
    }
}

void graph_add_vertex(Graph * g, void * data)
{
    if (g->length == g->n) { // need to reallocate for extra space
        g->n *= 2;
        g->vertices = realloc(g->vertices, g->n * sizeof(struct Vertex));
    }

    g->vertices[g->length].data = malloc(g->data_size);
    memcpy(g->vertices[g->length].data, data, g->data_size);
    list_init(&g->vertices[g->length].a, sizeof(struct Vertex *));
    g->length++;
}

void graph_add_edge(Graph * g, void * u, void * v)
{
    struct Vertex *p = &g->vertices[IDX_LABEL(*(char *)v)];
    /* the adjacency list stores pointers to struct Vertex, so get the Vertex address on p,
       and send the address of p so that we get a copy of it with memcpy() on list_append. 
       We don't want to copy the Vertex itself to the list, only its reference */
    list_append(&g->vertices[IDX_LABEL(*(char *)u)].a, &p);
    g->e++;
}

void graph_del_edge(Graph *g, void * u, void * v)
{
    struct Vertex *p = &g->vertices[IDX_LABEL(*(char *)v)];
    list_remove(&g->vertices[IDX_LABEL(*(char *)u)].a, &p);
    g->e--;
}
