# Conversion: Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.

def conversion(a, b):
    # xor to get a bit pattern with only the different bits set
    pattern = a ^ b
    # count the 1's in the pattern
    num_bits = 0
    while pattern and pattern != -1:
        if pattern % 2 != 0:
            num_bits += 1
        pattern >>= 1

    if pattern == -1:
        num_bits += 1

    return num_bits

def conversion2(a, b):
    pattern = a ^ b
    num_bits = 0
    while pattern and pattern != -1:
        # check if the lsb is 1:
        if pattern & 1: num_bits += 1
        pattern >>= 1

    if pattern == -1:
        num_bits += 1

    return num_bits