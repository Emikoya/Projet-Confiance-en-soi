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


fontType = ImageFont.truetype("font/times-ro.ttf", 24)

img = Image.new('RGB', (800, 480), color=(150, 150, 150))

draw = ImageDraw.Draw(img)
draw.text((300, 200), "Coucou toi ! Tu sais que je t'adore !",
          (0, 0, 0), font=fontType)

numberLastImage = lastImageNumber()
newLastImage = "./img/"+str(numberLastImage+1)+".png"
img.save(newLastImage)


# fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
# d = ImageDraw.Draw(img)
# d.text((10, 10), "Hello world", font=fnt, fill=(255, 255, 0))
