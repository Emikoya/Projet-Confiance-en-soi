from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

font = ImageFont.truetype("arial.pil")

img = Image.new('RGB', (600, 400), color='red')

draw = ImageDraw.Draw(img)
draw.text((300, 200), "Hello World !", (0, 0, 0), font=font)

img.save('image.png')
