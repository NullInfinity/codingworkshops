# This is an example of a library. Look through it in order to find functions that do what you
# need to do; you'll often do this since you don't want to reinvent the wheel. If something has
# already been done, it's much better to reuse than to redo, particularly since most libraries
# have been tried and tested many times.


# This library contains functions that can help you handle numbers of different formats and switch
# between them, e.g. from integer to binary to sequence of bits and back.

# converts binary numbers (e.g. bin(0b10)) to a regular integer (e.g. 2)
def binary_to_integer(b):
    return int(b,2)

# returns the last digit of the binary representation of a number (effectively the remainder of its division by 2):
def last_bit_of_binary(b):
    return int(b) % 2

# converts a binary number into an array of 8 binary (0 or ) digits in the same order (since ASCII codes for letters are 8 bits long)
def binary_to_bit_array(b):
    current_bin = int(b, 2)
    bits = []

    #why can't python do while loops :(
    if current_bin == 0:
        bits.append(0)

    #length of an ASCII is one byte, so 8 bits:
    while len(bits) != 8:
        bits.extend([current_bin % 2])
        current_bin /= 2

    bits.reverse()
    return bits

def bit_array_to_binary(bits):
    bits_left = bits.tolist()
    bits_left.reverse()
    current_bin = 0

    while len(bits_left > 0):
        current_bin = current_bin * 2 + bits_left[-1]
        bits_left = bits_left[:-1]

    return bin(current_bin)

# This information provided herein has been prepared by Morgan Stanley solely for use
# in connection with the Oxford Invariants coding workshop.