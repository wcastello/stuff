# Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
# possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

def pairwise_swap(num):
    # assume 32-bit num
    even_mask = 0x555555 # 0b01010101010101010
    odd_mask = 0xaaaa    # 0b10101010101010101
    even = num & even_mask # take only the even bits from num
    even <<= 1 # shift even bits to the left
    odd = num & odd_mask # take only the odd bits from num
    odd >>= 1 # shift odd bits to the right
    return even | odd # merge them and return