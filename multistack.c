#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int *arr;
    int numstacks;
    int size;
    int *top;
} MultiStack;

void mstack_init(MultiStack *s, int numstacks, int size);
bool mstack_push(MultiStack *s, int stacknum, int value);
int mstack_pop(MultiStack *s, int stacknum);

int main(void)
{
    MultiStack s;
    mstack_init(&s, 3, 3);

    for (int i = 0; i < 3; ++i) {
        for (int j = 13; j < 17; ++j) {
            printf("Trying to insert %d in stack %d\n", j, i);
            if (!mstack_push(&s, i, j))
                printf("Stack %d is full\n", i);
            else
                printf("Inserted %d in stack %d\n", j, i);
        }
    }

    int k;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            printf("Trying to pop from stack %d\n", i);
            k = mstack_pop(&s, i);
            printf("Popped %d from stack %d\n", k, i);
        }
    }
    return 0;
}

void mstack_init(MultiStack *s, int numstacks, int size)
{
    s->arr = malloc(numstacks*size*sizeof(int));
    s->numstacks = numstacks;
    s->size = size;
    s->top = malloc(numstacks*sizeof(int));

    for (int i = 0; i < numstacks; ++i)
        s->top[i] = i * size;
}

bool mstack_push(MultiStack *s, int stacknum, int value)
{
    // stack is full
    if (s->top[stacknum] == (stacknum+1)*s->size)
        return false;

    s->arr[s->top[stacknum]++] = value;
    return true;
}

int mstack_pop(MultiStack *s, int stacknum)
{
    // stack is empty
    if (s->top[stacknum] == stacknum * s->size) {
        printf("ERROR: Attempting to pop() from empty stack.\n");
        exit(EXIT_FAILURE);
    }
    return s->arr[--s->top[stacknum]];
}