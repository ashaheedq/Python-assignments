#
# ps7pr3.py (Problem Set 7, Problem 3)
#
# Image processing with loops and image objects
#
# Computer Science 111
# 

from cs111png import *

def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)            
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_rgb = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)

def brightness(rgb):
    """ takes the RGB values of a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    return (21*red + 72*green + 7*blue) // 100

### PUT YOUR WORK FOR PROBLEM 3 BELOW. ###

#Function 1
def bw(filename, threshold):
    """loads the PNG image file with the specified filename and creates a new image that is a black-and-white version of the original image.
       The second input to the function is a integer threshold between 0 and 255,
       and it should govern which pixels are turned white and which are turned black.
    """
    
    img = load_image(filename)

    height = img.get_height()
    width = img.get_width()

    for r in range(height):
        for c in range(width):
            rgb = img.get_pixel(r, c)            
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            
            luminosity = brightness (rgb)
            if luminosity > threshold:
                new_rgb = [255, 255, 255]
            elif luminosity < threshold:
                new_rgb = [0, 0, 0]
                
            img.set_pixel(r, c, new_rgb)

    new_filename = 'bw_' + filename
    img.save(new_filename)

#Function 2
def mirror_vert(filename):
    """ loads the PNG image file with the specified filename and creates
    a new image in which the original image is “mirrored” vertically. 
    """

    img = load_image(filename)

    height = img.get_height()
    width = img.get_width()

    for r in range(height//2):
        for c in range(width):
            rgb = img.get_pixel(r, c)            
            new_height = (height-1) -r
                
            img.set_pixel(new_height, c, rgb)

    new_filename = 'mirrorv_' + filename
    img.save(new_filename)

#function 3
def extract(filename, rmin, rmax, cmin, cmax):
    """loads the PNG image file with the specified filename and extracts a portion
    of the original image that is specified by the other four parameters.
    """
    new_height = (rmax-rmin)  
    new_width = (cmax-cmin)              
    new_img = Image(new_height, new_width)   # create a new, blank image object

    img = load_image(filename)

    height = new_img.get_height()
    width = new_img.get_width()
    
    for r in range(height):
        for c in range(width):
            rgb = img.get_pixel(r+rmin, c+cmin)            
                
            new_img.set_pixel(r, c , rgb)

    new_filename = 'extract_' + filename
    new_img.save(new_filename)
