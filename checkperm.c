#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>
#include <stdbool.h>

#define BE(t) (t ? "is" : "is not")

bool checkperm(char * s1, char * s2);
bool checkperm2(char * s1, char * s2);
int compar(const void *s1, const void *s2);

int main(int argc, char const *argv[])
{
    char s1[100], s2[100];
    scanf("%[^\n]%*c", s1);
    scanf("%[^\n]%*c", s2);
    bool ans;
    ans = checkperm2(s1, s2);
    printf("%s %s a permutation of %s\n", s1, BE(ans), s2);
    return 0;
}

/* Check if string a is a permutation of string b
   Return True if so, otherwise return False
   O(n) in time 
   O(1) in space (512 * sizeof(int) bytes)
   */
bool checkperm(char * s1, char * s2)
{
    unsigned int ta[256] = { 0 }, tb[256] = { 0 };
    char *s = s1;

    // O(n)
    while (*s1 != '\0' && *s2 != '\0') {
        ++ta[*s1];
        ++tb[*s2];
        s1++;
        s2++;
    }

    if (*s1 != '\0' || *s2 != '\0') { // different length, can't be a permutation
        printf("%c, %c\n", *s1, *s2);
        return false;
    }

    // O(n)
    while (*s != '\0') {
        if (ta[*s] != tb[*s])
            return false;
        s++;
    }

    return true;
}

/* Check if string a is a permutation of string b
   Return True if so, otherwise return False
   O(n*logn) in time
   O(n*logn) or O(n) in space because of the quicksort */
bool checkperm2(char * s1, char * s2)
{
    // O(n)
    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);

    if (len1 != len2)
        return false;

    // O(n*logn)
    qsort(s1, len1, sizeof(char), compar);
    qsort(s2, len2, sizeof(char), compar);

    return (strcmp(s1, s2) == 0);
}

int compar(const void *s1, const void *s2)
{
    return (*(char *)s1 >= *(char *)s2);
}