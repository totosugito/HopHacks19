from pdf2image import convert_from_path
import image_slicer
import PIL, os
from PIL import Image
import mathpix
import json

#Rotate the test image by 90 degrees to prepare for vertical cutting
def rotatePic():  
    picture= Image.open('out.jpg')

    picture.rotate(90, expand=True).save('rotated.jpg')
    os.remove('out.jpg')

#cut the rotated picture in half vertically, to simulate a horizontal cut on a pre-rotated paper
def slicePic():
    image_slicer.slice('rotated.jpg', 2)
    os.remove('rotated.jpg')

#cut the 2 pieces into 2 more pieces each to allow mathpix to easily consume the pictures
def slicePic2():
    image_slicer.slice('rotated_01_01.png', 2)
    image_slicer.slice('rotated_01_02.png', 2)
    os.remove('rotated_01_02.png')
    os.remove('rotated_01_01.png')

#rotate partitioned pieces of paper back to correct angle
def rotatePic2():
    picture1= Image.open('rotated_01_01_01_01.png')
    picture2= Image.open('rotated_01_01_01_02.png')
    picture3= Image.open('rotated_01_02_01_01.png')
    picture4= Image.open('rotated_01_02_01_02.png')

    picture1.rotate(270, expand=True).save('new_rotated1.png')
    picture2.rotate(270, expand=True).save('new_rotated2.png')
    picture3.rotate(270, expand=True).save('new_rotated3.png')
    picture4.rotate(270, expand=True).save('new_rotated4.png')

#delete all old files after creating new transformed files
    os.remove('rotated_01_01_01_01.png')
    os.remove('rotated_01_01_01_02.png')
    os.remove('rotated_01_02_01_01.png')
    os.remove('rotated_01_02_01_02.png')

if __name__ == "__main__":
    pages = convert_from_path('/Users/chuefengvang/Desktop/hophax/mathpix/api-examples-master/python_mvp/test_image.pdf', 500)
#converts the pdf into a jpg copy, makes manipulating easier and preserves original pdf copy
    for page in pages:
        page.save('out.jpg', 'JPEG')

    rotatePic()
    slicePic()
    slicePic2()
    rotatePic2()
