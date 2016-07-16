// Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. 
// Write code to find the length of the longest sequence of ls you could create.

#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

struct Flip flipbittowin(int num);
bool getbit(int num, int i);
int setbit(int num, int i);
int count_longest_set_bits(int num);
int msb_pos(int num);
int flipbittowin2(int num);

struct Flip {
    int longest_seq;
    int flip_pos;
};

int main(int argc, char const *argv[])
{
    int num, longest_a, longest_b;
    // scanf("%d", &num);
    for (num = -32768; num < 32768; ++num) {
        struct Flip f = flipbittowin(num);
        longest_a = f.longest_seq;
        longest_b = flipbittowin2(num);
        printf("num = %d, longest_a = %d, longest_b = %d\n", num, longest_a, longest_b);
        assert(longest_a == longest_b);
        printf("%d\n", flipbittowin2(num));
    }
    return 0;
}

struct Flip flipbittowin(int num)
{
    struct Flip flip = { .longest_seq = 0, .flip_pos = 0 };
    int set_bits;

    for (int i = 0; i <= msb_pos(num); ++i) {
        set_bits = count_longest_set_bits(setbit(num, i));
        if (set_bits > flip.longest_seq) {
            flip.longest_seq = set_bits;
            flip.flip_pos = i;
        }
    }
    return flip;
}

// O(b)
int msb_pos(int num)
{
    if (num < 0)
        return 4 * sizeof(num) - 1;

    int pos = 0;

    while (num >>= 1)
        pos++;
    
    return pos;
}

// return another integer, without modifying num
int setbit(int num, int i)
{
    return num | (1 << i);
}

bool getbit(int num, int i)
{
    return (num & (1 << i)) != 0;
}

int count_longest_set_bits(int num)
{
    int num_set_bits, max_set_bits;
    num_set_bits = max_set_bits = 0;

    for (int i = 0; i <= msb_pos(num); ++i) {
        if(getbit(num, i) == 0) {
            if (num_set_bits > max_set_bits) {
                max_set_bits = num_set_bits;
            }
            num_set_bits = 0;
        } else {
            num_set_bits += 1;
        }
    }
    num_set_bits = num_set_bits > max_set_bits ? num_set_bits : max_set_bits;
    return num_set_bits;
}

int flipbittowin2(int num)
{
    if (num == 0)
        return 1;

    int seq_sizes[4 * sizeof(num)], size, j;
    bool last_bit, curr_bit;
    last_bit = getbit(num, 0);
    size = 0, j = 0;

    for (int i = 0; i < 4 * sizeof(num); ++i) {
        curr_bit = getbit(num, i);
        if (curr_bit != last_bit) {
            seq_sizes[j++] = last_bit ? size : -1*size;
            size = 1;
        } else {
            size++;
        }
        last_bit = curr_bit;
    }

    if (curr_bit == last_bit)
        seq_sizes[j++] = last_bit ? size : -1*size;

    if (seq_sizes[j-1] < 0) // discard leading zeroes
        j--;

    int longest_seq, tmp, tmp_;
    tmp = tmp_ = longest_seq = 0;
    for(int i = 0; i < j; ++i) {
        if (seq_sizes[i] < 0) { // this is a zero sequence
            if (seq_sizes[i] == -1) { // of length 1, merge sides
                if (i > 0) tmp = seq_sizes[i-1];
                if (i < j-1) tmp += seq_sizes[i+1];
                tmp += 1;
            } else { // of length != 1, try adding 1 to each 1's sequence and see which one is larger
                if (i > 0) tmp = seq_sizes[i-1];
                if (i < j-1) tmp_ = seq_sizes[i+1];
                tmp = tmp > tmp_ ? 1 + tmp : 1 + tmp_;
            }
            if (tmp > longest_seq) {
                longest_seq = tmp;
            }
            tmp = tmp_ = 0;
        } else {
            if (seq_sizes[i] > longest_seq)
                longest_seq = seq_sizes[i];
        }
    }
    return longest_seq;
}
