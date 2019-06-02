import Image
import os

white = (255, 255, 255, 255)
grass = (72, 160, 72, 255)
yellow = (255, 255, 0, 255)

bgcolor = yellow

for file in os.listdir('.'):
	if not file.endswith('.png'):
		continue
	
	image = Image.open(file)
	if image.mode != 'RGBA':
		image = image.convert('RGBA')
	
	pixels = image.load()
	width = image.size[0]
	height = image.size[1]
	
	y = 0
	while y < height:
		x = 0
		while x < width:
			color = pixels[x, y]
			if color == bgcolor:
				pixels[x, y] = (0,0,0,0)
			x += 1
		y += 1
	
	image.save(file)