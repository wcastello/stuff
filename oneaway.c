#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#include <stdbool.h>

bool oneaway(char * s1, char * s2);
bool oneaway2(char * s1, char * s2);

int main(int argc, char const *argv[])
{
    char s1[100], s2[100];
    scanf("%[^\n]%*c", s1);
    scanf("%[^\n]%*c", s2);
    if (oneaway2(s1, s2))
        printf("one edit away!\n");
    else
        printf("not one edit away!\n");
}

/* Given two strings sa and sb check if they're 
   one insert, replace or remove away from each other.
   Return true if they are, otherwise return false.
*/
bool oneaway(char * s1, char * s2)
{
    int len1, len2;

    len1 = strlen(s1);
    len2 = strlen(s2);

    if (abs(len1 - len2) > 1)
        return false;

    if (len2 > len1) {
        int tmp = len2;
        len2 = len1;
        len1 = tmp;
        char *tmp_s = s1;
        s1 = s2;
        s2 = tmp_s;
    }

    for (int i = 0; i < len2; ++i) {
        if (s1[i] != s2[i]) {
            if (len1 == len2) /* replace */
                return (strcmp(&s1[i+1], &s2[i+1]) == 0);
            else {
                return (strcmp(&s1[i+1], &s2[i]) == 0);
            }
        }
    }

    return true;
}

bool oneaway2(char * s1, char * s2)
{
    int len1, len2;

    len1 = strlen(s1);
    len2 = strlen(s2);

    if (abs(len1 - len2) > 1)
        return false;

    if (len2 > len1) {
        int tmp = len2;
        len2 = len1;
        len1 = tmp;
        char *tmp_s = s1;
        s1 = s2;
        s2 = tmp_s;
    }

    for (int i = 0; i < len2; ++i) {
        if (s1[i] != s2[i]) {
            if (len1 == len2) { /* replace */
                for (int j = 0; s1[i+1+j] != '\0'; ++i) {
                    if (s1[i+1+j] != s2[i+1+j])
                        return false;
                }
                return true;
            }
            else { /* insert or delete */
                /* notice that inserting on the smaller one is the same as comparing
                   the bigger one but the actual char with the smaller from this position */
                /* removing from the bigger one is the same thing */
                /* and there's no removing from the smaller or adding to the bigger since
                   that would make the difference in the length too big for one away */ 
                for (int j = 0; s1[i+1+j] != '\0'; ++j) {
                    if (s1[i+1+j] != s2[i+j])
                        return false;
                }
                return true;
            }
        }
    }

    return true;
}

