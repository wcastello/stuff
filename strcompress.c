#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#include <stdbool.h>

char * strcompress(const char * s);
size_t cpy_last_and_count(char * dst, char last, int count);
char * itos(int num);

int main(int argc, char const *argv[])
{
    char s1[100];
    scanf("%[^\n]%*c", s1);
    char *s2 = strcompress(s1);
    printf("%s\n", s2);
    free(s2);
    return 0;
}

char * strcompress(const char * s)
{
    unsigned int count;
    size_t s_len, advc, comp_len = 0;
    char c, last, *comp, *curr;

    s_len = strlen(s);
    if (!s_len)
        return NULL;

    curr = comp = malloc(s_len);
    last = s[0];
    count = 0;

    while ((c = *s++) != '\0') {
        if (c == last) {
            count++;
            comp_len++;
        } else {
            advc = cpy_last_and_count(curr, last, count);
            curr += advc;
            comp_len += advc;
            count = 1;
        }
        last = c;
    }

    advc = cpy_last_and_count(curr, last, count);
    curr += advc;
    comp_len += advc;

    *curr = '\0';

    comp = realloc(comp, comp_len);
    return comp;
}

/* copy last char and count to the dst and return the number
   of bytes the dst pointer needs to advance in order to stay at
   the final position */
size_t cpy_last_and_count(char * dst, char last, int count)
{
    *dst++ = last;
    char *count_s = itos(count);
    size_t count_s_len = strlen(count_s);
    strncpy(dst, count_s, count_s_len);
    free(count_s);
    return count_s_len+1;
}

char * itos(int num)
{
    char buffer[11];
    char *s;
    int i = 0;
    do {
        buffer[i] = num % 10 + 48;
        ++i;    
    } while ((num /= 10) != 0);
    --i;

    s = malloc(i * sizeof(char));

    int j = 0;
    for (j = 0; i >= 0; --i, ++j)
        s[j] = buffer[i];

    s[j] = '\0';

    return s;
}