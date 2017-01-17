from image_utils import *
from array_utils import *
from number_utils import *

# after coding up a bunch of functions, it's a good idea to ensure they work properly
#  things like 0, empty lists or numbers that are too big are examples of edge cases, which should always be covered by tests

empty_string = ""
empty_array = []
empty_binary = 0b0

# apart from the edge cases, one should try to cover a good distribution of non-edge test cases as well
sample_string = "this is a string"

# for example, we aim to have both odd and even numbers, with binary representations ending in both 1 and 0
# we also want both small and large numbers

integer_array = [0, 1, 23, 65, 99, 234, 23152]
binary_array = [bin(0b0), bin(0b1), bin(0b10111), bin(0b1000001), bin(0b1100011), bin(0b11101010), bin(0b101101001110000)]

# we need a short string to test, which is simple to convert to its ascii code representation
# all of therse are the same information represented in 3 different formats
short_string = "short"
short_ascii_string = [115, 104, 111, 114, 116]
short_binary_array = [bin(0b01110011), bin(0b01101000), bin(0b01101111), bin(0b01110010), bin(0b01110100)]

sample_image_filename = "..\\resources\\map.bmp" # width x height

#the following are examples of what we call unit tests - small bits of code that test small bits of functionality
# piece by piece so that we know it's all correct


#testing image_to_array
loaded_image = load_image_to_array(sample_image_filename)
assert loaded_image.shape == (width, height, 3) # change these to actual ints!

#testing image_to_flat_array
arr, rows, cols = load_image_to_flat_array(sample_image_filename)
assert arr.shape[0] = 3 * rows * cols

#testing flat_array_to_rgb
rgb = flat_array_to_rgb(arr, rows, cols)
for i in range(0, rows):
    for j in range(0, cols):
        for k in range(0, 3):
            assert(rgb[i][j][k] == loaded_image[i][j][k])

# no need to test saving, flattening or reshaping since they are functions provided to us

# testing string_to_ascii_array
assert(string_to_ascii_array(short_string) == short_ascii_string)
assert(string_to_ascii_array(empty_string) == empty_array)

#testing ascii_array_to-string
assert(ascii_array_to_string(short_ascii_string)) == short_string
assert(ascii_array_to_string(empty_array)) == empty_string

#testing binary to integer
assert(binary_to_integer(bin(0b0)) == 0)
assert(binary_to_integer(bin(0b1)) == 1)
assert(binary_to_integer(bin(0b1100011)) == 99)
assert(binary_to_integer(bin(0b11101010)) == 234)

#testing last bit
assert(last_bit_of_binary(0) == 0)
assert(last_bit_of_binary(115) == 1)
assert(last_bit_of_binary(2)== 0)

#testing integer_array_to_binary

assert(integer_array_to_binary(integer_array) == binary_array)
assert(integer_array_to_binary(binary_array_to_integer(binary_array)) == binary_array)

# testing binary array to integer
assert(binary_array_to_integer(binary_array) == integer_array)
assert(binary_array_to_integer(integer_array_to_binary(integer_array)) == integer_array)

# testing binary_to_bit_array - note these arrays should be eight entries long
assert(binary_to_bit_array(bin(0)) == [0, 0, 0, 0, 0, 0, 0, 0])
assert(binary_to_bit_array(bin(1)) == [0, 0, 0, 0, 0, 0, 0, 1])
assert(binary_to_bit_array(bin(2)) == [0, 0, 0, 0, 0, 0, 1, 0])
assert(binary_to_bit_array(bin(64)) == [0, 1, 0, 0, 0, 0, 0, 0])
assert(binary_to_bit_array(bin(0b10111)) == [0, 0, 0, 1, 0, 1, 1, 1])
assert(binary_to_bit_array(bin(0b01110000)) == [0, 1, 1, 1, 0, 0, 0, 0])


# (2) now write a few test cases to test conversion of bit arrays into numbers

# This information provided herein has been prepared by Morgan Stanley solely for use
# in connection with the Oxford Invariants coding workshop.