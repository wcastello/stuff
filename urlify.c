#include <stdio.h>
#include <string.h>
#include <inttypes.h>
#include <stdbool.h>

char * urlify(char * s);
char * urlify2(char * s);
char * urlify3(char * s);

int main(int argc, char const *argv[])
{
    char string[100];
    scanf("%[^\n]%*c", string);
    printf("%s\n", urlify3(string));
}

/* Replace all whitespaces with %20 in place and return the modified string.
   Assume that s has enough space to hold the aditional characters.
*/
char * urlify(char * s)
{
    size_t len = strlen(s);
    char buffer[len];
    for (int i = 0; i < len; ++i) {
        if (s[i] == ' ') {
            int j;
            for (j = 0; j < len - i; ++j)
                buffer[j] = s[i+1+j];       // strlen() returns the number of chars that
            s[i] = '%';                     // precede the '\0', but we also want to copy it
            s[i+1] = '2';
            s[i+2] = '0';
            for (j = 0; j < len - i; ++j)
                s[i+3+j] = buffer[j];
            urlify(&s[i+3]);
            break;
        }
    }
    return s;
}

char * urlify2(char * s)
{
    size_t len = strlen(s);
    char buffer[len-1];
    for (int i = 0; i < len; ++i) {
        if (s[i] == ' ') {
            int j;
            memmove(&s[i+3], &s[i+1], len-i);
            s[i] = '%';
            s[i+1] = '2';
            s[i+2] = '0';
            urlify(&s[i+3]);
            break;
        }
    }
    return s;
}

// working backwards
char * urlify3(char * s)
{
    int i, j, whitespaces;
    for (i = 0, whitespaces = 0; s[i] != '\0'; ++i) {
        if (s[i] == ' ')
            ++whitespaces;
    }

    size_t len = strlen(s);
    size_t newlen = len + 2 * whitespaces;

    for (i = 0, j = newlen; i <= len; ++i) {
        printf("%c and %c\n", s[len-i], s[newlen-i]);
        if (s[len - i] == ' ') {
            printf("whitespace\n");
            s[j] = '0';
            s[j - 1] = '2';
            s[j - 2] = '%';
            j -= 3;
        } else {
            s[j--] = s[len - i];
        }
    }

    return s;
}