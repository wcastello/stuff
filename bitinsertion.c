#include <stdio.h>
#include <stdbool.h>
#include "stack.h"

void insertion(int * m, int * n, int i, int j);
void setbit(int * n, int i);
bool getbit(int n, int i);
void clearbit(int * n, int i);
void updatebit(int * n, int i, bool b);

void dec2bin(int n, char * dec);

int main(int argc, char const *argv[])
{
    int m, n, i, j;
    char bitm[32], bitn[32];
    scanf("%d%d%d%d", &m, &n, &j, &i);
    dec2bin(n, bitn);
    dec2bin(m, bitm);
    printf("before: m = %s, n = %s\n", bitm, bitn);
    insertion(&m, &n, i, j);
    dec2bin(n, bitn);
    dec2bin(m, bitm);
    printf("after: n = %s\n", bitn);

    return 0;
}

// insert m into n such that m starts at bit j and ends at bit i
// j >= i
void insertion(int * m, int * n, int i, int j)
{
    bool b;
    for (int k = 0; k < j - i + 1; k++) {
        // get bit k from m
        b = getbit(*m, k);
        // use it to set bit k + j on n
        updatebit(n, j - k, b);
    }
}

void updatebit(int * n, int i, bool b)
{
    if (b)
        setbit(n, i);
    else
        clearbit(n, i);
}

void clearbit(int * n, int i)
{
    *n = *n & ~(1 << i);
}

void setbit(int * n, int i)
{
    *n = *n | (1 << i);
}

bool getbit(int n, int i)
{
    return n & (1 << i);
}

void dec2bin(int n, char * dec)
{
    Stack s;
    stack_init(&s, sizeof(char), NULL);
    int c;
    while (n) {
        c = n % 2 + 48;
        stack_push(&s, &c);
        n /= 2;
    }

    while (!stack_empty(&s))
        *dec++ = *(char *)stack_pop(&s);

    *dec = '\0';
}
