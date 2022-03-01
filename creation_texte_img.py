# IMPORT
import os
from PIL import Image, ImageDraw, ImageFont

# Create image with text inside


# Search number for new image

def lastImageNumber():
    last = 0
    dir = "./img"
    for path in os.listdir(dir):
        last = last + 1
    return last

# Create image


img = Image.new('RGB', (100, 30), color=(73, 109, 137))

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello world", font=fnt, fill=(255, 255, 0))

newLastImage = './img//'+lastImageNumber+1+'.png'
img.save(newLastImage)
