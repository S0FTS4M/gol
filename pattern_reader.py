# Python program to read image using OpenCV

# importing OpenCV(cv2) module
from math import fabs
from turtle import right, width
from PIL import Image, ImageOps

img = Image.open('patterns/inf_glider_pattern.png')
img = ImageOps.grayscale(img)
width, heigth = img.size
print((width, heigth))

pic = []


def find_thickness_of_line(row, col):
    thickness = 0
    for r in range(row, heigth):
        for c in range(col, width):
            val = img.getpixel((c, r))
            if val == 255:
                return thickness
            else:
                thickness += 1


def detect_sizeof_cell(img):
    found_cell = False
    finished_cell = False
    cell_size = 0
    for row in range(heigth):
        pic.append([])
        for col in range(width):
            if found_cell and finished_cell:
                thickness = find_thickness_of_line(row, col)
                return (cell_size, thickness)
            val = img.getpixel((col, row))
            pic[row].append(val)

            if found_cell == False and val == 255:
                found_cell = True
            elif found_cell and val == 255:
                cell_size += 1
            elif found_cell and val != 255:
                finished_cell = True


def read_pattern():
    size, thickness = detect_sizeof_cell(img)

    total_cell_size = size + thickness
    print(size, thickness)
    dead=0
    alive=0
    cell_count = 0
    for row in range(thickness, heigth, total_cell_size):
        for col in range(thickness, width, total_cell_size):
            # print(row, col)
            val = img.getpixel((col + thickness, row + thickness))
            print(val)
            if val == 0:
                alive += 1
            else:
                dead += 1
            cell_count += 1

    print(cell_count)
    print(dead,alive)

    print(5)


def write_to_txt():
    with open("output.txt", "w") as f:
        for i in range(heigth):
            for j in range(width):
                f.write(str(pic[i][j]) + " ")
            f.write("\n")


read_pattern()
