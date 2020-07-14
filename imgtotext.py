import pytesseract
import os
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Path to the tesseract 

def convert():
    img = Image.open('img.jpg')
    text = pytesseract.image_to_string(img)
    print(text)

convert()
