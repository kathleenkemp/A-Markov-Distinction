"""
Kathleen Kemp
CS3725
2/26/21

"""

from PIL import Image
import numpy as np

my_image = Image.open('monet.jpg')

# get RGB values of pixels from numpy array by passing in image (convert image to numpy array)
numpypixels = np.asarray(my_image)

# taking 3D array and converting to 2D (1st D: rows*columns=length, 2nd D: filled with pixel)
# e.g. (128 x 128 x 3) => (128 * 128 x 3) in order to find each unique pixel value
flattened = numpypixels.reshape(numpypixels.shape[0]*numpypixels.shape[1], numpypixels.shape[2])

# getting unique values across 1st D
uniques = np.unique(flattened, axis=0)
print("number of unique pixels: ", len(uniques)) # ~54,000

# random number generator to pick a pixel
rng = np.random.default_rng()

# initialize empty list, looping through numpy array of same size
# as the output image and filling in a random pixel, saving the image
# to the same directory
for i in range(5):
    output = []
    for row in numpypixels:
        new_row = []
        for pixel in row:
            chosen_pixel = rng.choice(uniques, axis=0)
            new_row.append(chosen_pixel)
        output.append(new_row)
    output = np.array(output)
    new_img = Image.fromarray(output)
    # save image with index of loop
    new_img.save("my_new_image_"+i+".jpg")
    
print("created images successfully")