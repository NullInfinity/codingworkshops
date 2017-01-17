# This is an example of a library. Look through it in order to find functions that do what you
# need to do; you'll often do this since you don't want to reinvent the wheel. If something has
# already been done, it's much better to reuse than to redo, particularly since most libraries
# have been tried and tested many times.

import numpy as np

# this library contains functions to help you work with arrays and convert them between different formats of data they can store

# converts arrays of integers (e.g. [0, 4, 10]) into binary representations (e.g. [0, 10, 110])
def integer_array_to_binary(ints):
    return [bin(i) for i in ints]

# converts arrays of binar numbers back into arrays of integers (e.g. [0, 1, 2])
def binary_array_to_integer(bins):
    # (1) use a for comprehension to implement this function
    # (hint: such a conversion is done somewhere else in the code :) )
    return # something


# transforms an array of arrays into a single array of all elements contained in them
def flatten(arr):
    return np.array(np.array(arr).flatten())

# ascii characters are 8 bits long so we need to collect every 8 bits into an array to convert into ascii
def group_bits_into_characters(arr):
    return np.array(arr).reshape(-1, 8)

# convert a string into numerical (ascii) representations which are then easy to convert to binary:
def string_to_ascii_array(string):
    return [ord(c) for c in string]

# inverse of the above, from numerical representations to strings
def ascii_array_to_string(array):
    return ''.join([chr(i) for i in array])

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
# THIS SOFTWARE IS PRO