from image_utils import *
from number_utils import *
from array_utils import *
from system import argv as arguments

# tip: when in doubt about what something does, print it out

# image represents path to the bitmap image in which we embed the hidden message

def hide(image_path, message, output_path):
    # first load up the image
    image_array, rows, columns = load_image_to_flat_array(image_path)

    # deal with the trivial case
    if len(message) == 0:
        result = flat_array_to_rgb(image_array, rows, cols)
        save_rgb_array_to_image(output_path, result)
        return 0

    # (3) now transform the message into an array of binary numbers:

    message_binaries = []
    message_bits = flatten([binary_to_bit_array(b) for b in message_binaries])

    # (4) compute key as size of image array over length of the message, note potential division by 0 handled above

    key = 0

    # (5) implement a for loop with if, else to do actual hiding



    # (6) generate, based on the key, the positions in the image array that we use for hiding, and set their last
    # binar digit to the appropriate bit in the message bits


    # finally, turn the array thus obtained into a new image which we save
    result = flat_array_to_rgb(image_array, rows, columns)
    save_rgb_array_to_image(output_path, result)

    # and print the key
    return key

# usage: python hider.p path/to/image "message to hide" path/to/resulting/image

if __name__ == "__main__":
    img_path = arguments.argv[1]
    msg = arguments.argv[2]
    out_path = arguments.argv[3]
    k = hide(img_path, msg, out_path)

    print "*** KEY FOR HIDDEN MESSAGE ***"
    print key
    print "******************************"



    # This information provided herein has been prepared by Morgan Stanley solely for use
    # in connection with the Oxford Invariants coding workshop.