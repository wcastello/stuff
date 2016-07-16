#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

char * doublebit2str(double num);

int main(int argc, char const *argv[])
{
    double num;
    scanf("%lf", &num);
    printf("%s\n", doublebit2str(num));

    return 0;
}

char * doublebit2str(double num)
{
    char *s = malloc(35 * sizeof(char));
    int i = 0;
    char c;
    bool fit = true;;
    *s++ = '0';
    *s++ = '.';
    while (num > 0) {
        if (i > 32) {
            *s++ = '(';
            *s++ = '.';
            *s++ = '.';
            *s++ = '.';
            *s++ = ')';
            fit = false;
            break;
        }
        num *= 2;
        *s++ = (int)num/1 + 48;
        if (num >= 1)
            num -= 1;
        ++i;
    }
    *s = '\0';
    s = (fit) ? s-(i+2) : s-(i+7);
    return s;
}