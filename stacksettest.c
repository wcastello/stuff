#include <stdio.h>
#include "stackset.h"

int main(int argc, char const *argv[])
{
    int arr[] = {10, -15, 3, 2, 5, -2, 1, -1, -2, -3, -3, -10};
    int len = sizeof(arr)/sizeof(int);
    StackSet s;
    stackset_init(&s, sizeof(int), 4);
    for (int i = 0; i < len; ++i) {
        printf("Pushing %d\n", arr[i]);
        stackset_push(&s, &arr[i]);
        printf("Stack: ");
        stackset_int_print(&s);
        if (!stackset_empty(&s))
            printf("stack_peek: %d\n",*(int *)stackset_peek(&s));
    }

    while (!stackset_empty(&s)) {
        void *data = stackset_pop(&s);
        printf("Popped %d, freeing it.\n", *(int *)data);
        printf("Stack: ");
        stackset_int_print(&s);
        if (!stackset_empty(&s))
            printf("stack_peek: %d\n", *(int *)stackset_peek(&s));
    }
    return 0;
}
