import pytesseract as tess
from PIL import Image
image = Image.open('pic.JPG')

text = tess.image_to_string(image)
print(text)
print('123abc')
print(tess.__version__)
##data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')