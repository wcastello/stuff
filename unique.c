#include <stdio.h>
#include <string.h>
#include <inttypes.h>
#include <stdbool.h>

bool unique(char * s);
bool unique2(char * s);
bool unique3(char * s);

int main(int argc, char const *argv[])
{
    char string[100];
    scanf("%[^\n]%*c", string);
    if (unique3(string))
        printf("all unique chars.\n");
    else
        printf("not all unique chars.\n");
    return 0;
}

/* Determine if a string has all unique characters.
   Assume s is a string composed only of ASCII characters.
   Return true if it has, false otherwise. 
   Uses a direct-address table */
bool unique(char * s)
{
    int i;
    bool chars[256] = { false };

    /* using strlen() would make unique() run through the string more
       than necessary */
    while (*s != '\0') {
        if (chars[*s])
            return false;
        chars[*s] = true;
        ++s;
    }

    return true;
}

/* Determine if a string has all unique characters.
   Assume s is a string composed only of ASCII characters.
   Return true if it has, false otherwise. */
bool unique2(char * s)
{
    for (int i = 0; i < strlen(s); ++i) {
        for (int j = i+1; j < strlen(s); ++j) {
            if (s[i] == s[j])
                return false;
        }
    }

    return true;
}

bool unique3(char * s)
{
    uint64_t t[4] = { 0 }; // 256 bits, one for each char
    while (*s != '\0') {
        if ( (1 << (*s % 64)) & t[*s / 64] )
            return false;
        t[*s / 64] |= (1 << (*s % 64));
        s++;
    }

    return true;
}