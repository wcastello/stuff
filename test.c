#include <stdio.h>
#include <stdlib.h>

struct S {
    int a;
    int b;
    int c;
    int d;
    char chr;
};

int main(int argc, char const *argv[])
{
    struct S **s = malloc(10 * sizeof(struct S *));
    for (int i = 0; i < 10; ++i) {
        s[i] = malloc(sizeof(struct S));
        s[i]->a = i;
        s[i]->b = i+1;
        s[i]->c = i+2;
        s[i]->d = i+3;
        s[i]->chr = 'a' + i;
    }

    for (int i = 0; i < 10; ++i) {
        printf("%d, %d, %d, %d, %c\n", s[i]->a, s[i]->b, s[i]->c, s[i]->d, s[i]->chr);
    }


    return 0;
}