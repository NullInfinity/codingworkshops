import numpy as np
from PIL import Image

# This is an example of a library. Look through it in order to find functions that do what you
# need to do; you'll often do this since you don't want to reinvent the wheel. If something has
# already been done, it's much better to reuse than to redo, particularly since most libraries
# have been tried and tested many times.

# this library contains functions to help you handle image conversions

# load an image and transform it into an array of size WIDTH x HEIGHT x 3
# so load_image_to_arra(path)[row][col] is an array of 3 numbers in the range 0-255
# first pixel is red, second is green and 3rd is blue, the 3 making up a single pixel

if __name__ == '__main__':
    def load_image_to_array(path):
        img = Image.open(path)
        return np.array(img)

    # returns image as a flat array of numbers, row count, column count
    # by flat array we mean the sequence is R, G, B, R, G, B, R,

def load_image_to_flat_array(path):
    arr = load_image_to_array(path)
    (rows, columns, _) = arr.shape
    #array ( array ( array () ) )
    # row     pixel   color
    return np.array(arr.flatten()), rows, columns

# the reverse of the above: given rows and columns, turn the array of numbers into an array
# of [R, G, B] arrays, each representing a single pixel

def flat_array_to_rgb(arr, rows, columns):
    return arr.reshape(rows, columns, 3)

# simply provide the path e.g. "C:\Windows\image.jpg" - note: \ is a special character with a
# different meaning, so we need to escape it by using \\ instead of just \; the 2nd argument
# is just the array we pass as the image itself
def save_rgb_array_to_image(path, array):
    Image.fromarray(array, "RGB").save(path)
    return #nothing


# This information provided herein has been prepared by Morgan Stanley solely for use
# in connection with the Oxford Invariants coding workshop.

# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.Numpy Copyright (c) 2005, NumPy Developers
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# Neither the name of the NumPy Developers nor the names of any contributors may be used to endorse or promote products derived from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE