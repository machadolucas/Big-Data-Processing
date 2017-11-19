from PIL import Image, ImageFilter
from sklearn import svm, datasets
import numpy as np


# Function to receive an image filename, and return a flattened list of values after processing.
def process_image(filename):
    # Load the image from filename
    img = Image.open(filename).convert('RGB')
    pix = img.load()

    # Isolate the digit from the image background (and transform to black and white). Also detect content boundaries.
    boundaries = [img.width, img.height, 0, 0]
    for x in range(0, img.width):
        for y in range(0, img.height):
            pixel = pix[x, y]
            if (pixel[0] + 15 <= pixel[2]) and (pixel[1] + 15 <= pixel[2]):
                pix[x, y] = (0, 0, 0)  # Transform to black.

                if x < boundaries[0]:  # Get leftmost index of content.
                    boundaries[0] = x
                if y < boundaries[1]:  # Get upper index of content.
                    boundaries[1] = y
                if x > boundaries[2]:  # Get rightmost index of content.
                    boundaries[2] = x
                if y > boundaries[3]:  # Get lower index of content.
                    boundaries[3] = y
            else:
                pix[x, y] = (255, 255, 255)  # Transform to white.

    # Crop the image by detected boundaries and ensure that the image dimensions correspond to a square.
    content_size = (boundaries[2] - boundaries[0], boundaries[3] - boundaries[1])
    square_size = max(content_size[0], content_size[1])
    square_img = Image.new("RGB", (square_size, square_size), color=(255, 255, 255))
    paste_coords = tuple([int(square_size / 2 - content_size[0] / 2), int(square_size / 2 - content_size[1] / 2)])
    square_img.paste(img.crop(tuple(boundaries)), box=paste_coords)

    # Resize the image to 16x16 pixels, convert it to a greyscale image, and filter it with ImageFilter.Kernel.
    square_img = square_img.resize((16, 16)).convert('L')
    square_img = square_img.filter(
        ImageFilter.Kernel((3, 3), [0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625]))

    # Create a new 8x8 2D list where the value [j,i] is given the average value of the four pixels from processed image.
    img_matrix = [[0 for x in range(8)] for y in range(8)]
    sq_img_px = square_img.load()
    for i in range(8):
        for j in range(8):
            img_matrix[j][i] = np.mean(
                [sq_img_px[2 * i, 2 * j], sq_img_px[2 * i + 1, 2 * j],
                 sq_img_px[2 * i, 2 * j + 1], sq_img_px[2 * i + 1, 2 * j + 1]])

    # Transform the pixel values to be between 0..16, where 0 means white and 16 means black.
    for i in range(8):
        for j in range(8):
            img_matrix[i][j] = (256 - img_matrix[i][j]) / 16

    # Convert the 8x8 image into a 1D list of 8*8 = 64 values, and return it.
    list_1d = sum(img_matrix, [])
    return list_1d


# Load whole datasets from sklearn and do the training of the classifier
digits = datasets.load_digits()
classifier = svm.SVC(gamma=0.001)
classifier.fit(digits.data, digits.target)

# Process all given images
# The 'digits' folder with *.png files is assumed to be in the same place as this digimatch.py file
filenames = ['digits/' + str(x) + '.png' for x in range(0, 10)]
processed_images = [process_image(filename) for filename in filenames]

# Predict from images, calculate accuracy and print results.
results = classifier.predict(processed_images)

correct = len([p for p, a in zip(list(range(10)), results) if p == a])
accuracy = correct / len(results) * 100

print('Expected numbers (in order):')
print(list(range(10)))

print('Predicted numbers:')
print(list(results))

print('Accuracy: ' + str(round(accuracy, 2)) + '%')
