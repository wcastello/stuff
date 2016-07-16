#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#include <stdbool.h>

int substr(char * string, char * substring);

int main(int argc, char const *argv[])
{
    char s1[100], s2[100];
    scanf("%[^\n]%*c", s1);
    scanf("%[^\n]%*c", s2);
    printf("%d\n", substr(s1, s2));
}

/* 
*/
int substr(char * string, char * substring)
{
    bool diff;
    size_t slen = strlen(string);
    size_t sublen = strlen(substring);
    for (int i = 0; i < slen - sublen + 1; ++i) {
        diff = false;
        for (int j = 0; j < sublen; ++j) {
            printf("(%c, %c) ", string[i+j], substring[j]);
            if (string[i+j] != substring[j]) {
                diff = true;
                break;
            }
        }
        printf("\n");
        if (diff)
            continue;
        return i;
    }
    return -1;
}