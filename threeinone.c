#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define STACKSIZE 3

typedef struct {
    int arr[3*STACKSIZE];
    int top[3], base[3];
} TripleStack;

void tstack_init(TripleStack *s);
bool tstack_push(TripleStack *s, int stack_num, int value);
int tstack_pop(TripleStack *s, int stack_num);

int main(void)
{
    TripleStack s;
    tstack_init(&s);

    for (int i = 0; i < 3; ++i) {
        for (int j = 13; j < 17; ++j) {
            printf("Trying to insert %d in stack %d\n", j, i);
            if (!tstack_push(&s, i, j))
                printf("Stack %d is full\n", i);
            else
                printf("Inserted %d in stack %d\n", j, i);
        }
    }

    int k;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < STACKSIZE; ++j) {
            printf("Trying to pop from stack %d\n", i);
            k = tstack_pop(&s, i);
            printf("Popped %d from stack %d\n", k, i);
        }
    }
    return 0;
}

void tstack_init(TripleStack *s)
{
    for (int i = 0; i < 3; ++i)
        s->base[i] = s->top[i] = i*STACKSIZE;
}

bool tstack_push(TripleStack *s, int stack_num, int value)
{
    // stack is full
    if (s->top[stack_num] == (stack_num+1)*STACKSIZE)
        return false;

    s->arr[s->top[stack_num]++] = value;
    return true;
}

int tstack_pop(TripleStack *s, int stack_num)
{
    // stack is empty
    if (s->top[stack_num] == s->base[stack_num]) {
        printf("ERROR: Attempting to pop() from empty stack.\n");
        exit(EXIT_FAILURE);
    }
    return s->arr[--s->top[stack_num]];
}