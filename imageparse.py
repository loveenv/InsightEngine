import pytesseract as tess
from PIL import Image
img = Image.open('IMG_20160506_181223.JPG')
text = tess.image_to_string(img)
print(text)
print('123abc')
print(tess.__version__)
##data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')