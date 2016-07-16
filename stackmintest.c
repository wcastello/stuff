#include <stdio.h>
#include "stack.h"

int compar_int(const void * a, const void * b);

int main(int argc, char const *argv[])
{
    int arr[] = {10, -15, 3, 2, 5, -2, 1, -1, -2, -3, -3, -10};
    int len = sizeof(arr)/sizeof(int);
    Stack s;
    stack_init(&s, sizeof(int), compar_int);
    for (int i = 0; i < len; ++i) {
        printf("Pushing %d\n", arr[i]);
        stack_push(&s, &arr[i]);
        printf("Stack: ");
        stack_int_print(&s);
        printf("Stack mins: ");
        list_int_print(s.mins);
        if (!stack_empty(&s))
            printf("stack_peek: %d\n",*(int *)stack_peek(&s));
    }

    while (!stack_empty(&s)) {
        void *data = stack_pop(&s);
        printf("Popped %d, freeing it.\n", *(int *)data);
        printf("Stack: ");
        stack_int_print(&s);
        printf("Stack mins: ");
        list_int_print(s.mins);
        if (!stack_empty(&s))
            printf("stack_peek: %d\n", *(int *)stack_peek(&s));
    }
    return 0;
}

int compar_int(const void * a, const void * b)
{
    return *(int *)a - *(int *)b;
}