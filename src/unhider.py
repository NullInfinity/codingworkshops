from image_utils import *
from array_utils import *
from number_utils import *
from sys import argv as arguments

# image represents the path to the bitmap image containing the hidden message
# key is a number that tells the program the distance between two consecutive pixels
# containing bits of the hidden message


def unhide(image_path, k):
    # (7) we use key 0 for empty messages, so deal with this case

    message = ""

    # (8) start by loading image up:



    # (9) implement rest of this function using calls to helpers :)



    # (10) the key tells you every which bits we find something, so use it to find message length
    # hint: you'll need the size of the image



    # (11) read every kth pixel and add to the message bits the last bit of the pixel


    # every character is 8 bits long, so we pack up into groups of 8
    binary_character_arras = group_bits_into_characters(message_bits)

    # now turn each group of 8 into one binary number:



    # now convert the binary numbers into integers (should be 1 function call :) )


    message = ascii_array_to_string(ascii_characters)

    return message


# usage: python unhider.py path/to/image 123456
if __name__ == "main":
    input_path = arguments[1]
    key = arguments[2]
    output = unhide(input_path, key)
    print output