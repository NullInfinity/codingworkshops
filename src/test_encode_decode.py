from hider import *
from unhider import *
from image_utils import load_image_to_flat_array

# this tests correctness of the 2 methods, hide and unhide
# similar to the unit tests in test_helper, but more complex
# we call this an integration test since it tests how the components work together

img_path = "..\\resources\\map.bmp"
message = "this is a sample message"
empty_message = ""

output_msg = "..\\resources\\sample.bmp"
output_empty = "..\\resources\\empty.bmp"

key_sample = hide(img_path, message, output_msg)
key_empty = hide(img_path, empty_message, output_empty)
# empty case not yet handled

assert(unhide(output_empty, key_empty) == empty_message)
assert(unhide(output_msg, key_sample) == message)

# finally, for the empty case, test that images are identical
original_img_flat_array, rows, cols = load_image_to_flat_array(img_path)
output_img_flat_array, rows, cols = load_image_to_flat_array(output_empty)

assert(output_rows == rows and output_cols == cols)
for i in range(0, 3 * rows * cols):
    assert original_img_flat_array[i] == output_img_flat_array[i]

# This information provided herein has been prepared by Morgan Stanley solely for use
# in connection with the Oxford Invariants coding workshop.