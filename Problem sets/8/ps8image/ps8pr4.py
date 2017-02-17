#
# ps8pr4.py (Problem Set 8, Problem 4)
#
# Images as 2-D lists
#
# Computer Science 111
#

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def  blank_image(height, width):
    '''creates and returns a 2-D list of pixels with height rows and width columns
    in which all of the pixels are green
    '''
    image = create_uniform_image(height, width, [0,255,0])

    return image

def flip_vert(pixels):
    '''takes the 2-D list pixels containing pixels for an image, and that creates
        and returns a new 2-D list of pixels for an image in which the original image is “flipped” vertically
    '''
    height = len(pixels)
    width = len(pixels[0])
    inverted_image = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            inverted_image[r-1][c] = pixels[-r][c]

    return inverted_image

def reduce(pixels):
    """takes the 2-D list pixels containing pixels for an image, and that creates
    and returns a new 2-D list that represents an image that is
    half the size of the original image.
    """
    height = len(pixels)
    width = len(pixels[0])
    reduced_image = blank_image(height//2, width//2)
    for r in range(height//2):
        for c in range(width//2):
            reduced_image[r][c] = pixels[r*2][c*2]

    return reduced_image

def transpose(pixels):
    """takes the 2-D list pixels containing pixels for an image,
    and that creates and returns a new 2-D list that is the transpose of pixels
    """
    height = len(pixels)
    width = len(pixels[0])

    transposed_image = blank_image(width, height)

    for i in range(width):
        for c in range(height):
            transposed_image[i][c] = pixels[c][i]
    return transposed_image

def rotate_clockwise(pixels):
    """rotate the original image clockwise by 90 degrees
    """

    rotated_image = transpose(pixels)

    return rotated_image

def rotate_counterclockwise(pixels):
    """should rotate the original image counterclockwise by 90 degrees
    """

    rotated_image = flip_vert(pixels)

    rotated_image = transpose(rotated_image)
    return rotated_image
