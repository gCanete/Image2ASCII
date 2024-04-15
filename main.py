from PIL import Image
import numpy as np
import sys


filename = sys.argv[1]
CHARS = [' ', '"', '+', '$']
MAX_WIDTH = 800
MAX_HEIGHT = 500


def img2matrix(file_path):
    img = Image.open(file_path).convert('L')
    width, height = img.size
    aspect_ratio = width/height

    maximum = lambda width, height: width if width > height else height
    max_dim = maximum(width, height)

    if max_dim > MAX_WIDTH:
        # Resize based on width
        width = MAX_WIDTH
        height = round(width / aspect_ratio)
        img = img.resize((width, height), Image.LANCZOS)

        if max_dim > MAX_HEIGHT:
            height = MAX_HEIGHT
            width = round(height * aspect_ratio)
            img = img.resize((width, height), Image.LANCZOS)

    img_matrix = np.zeros((width, width))

    for col in range(width):
        for row in range(height):
            img_matrix[col][row] = img.getpixel((col, row))
    return img_matrix



def img2ascii(img_matrix):
    width, height = img_matrix.shape

    for row in range(height):
        print()
        for col in range(width):
            if img_matrix[col][row] < 64:
                print(CHARS[0], end=" ")
            elif (img_matrix[col][row] >= 64) & (img_matrix[col][row] < 128):
                print(CHARS[1], end=" ")
            elif (img_matrix[col][row] >= 128) & (img_matrix[col][row] < 192):
                print(CHARS[2], end=" ")
            else:
                print(CHARS[3], end=" ")



if __name__ == '__main__':
    mat = img2matrix(filename)
    img2ascii(mat)

