import pytesseract as tess
from PIL import Image
img = Image.open('pic.JPG')
##img.show()
##text = tess.image_to_string(img)
text = tess.image_to_string('pic.JPG')
print(text)
##print('123abc')
##print(tess.__version__)
##data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')