import Image
import os

for file in os.listdir('.'):
	if not file.endswith('.png'):
		continue
	
	img = Image.open(file)
	if img.mode != 'RGBA':
		img = img.convert('RGBA')
	
	width = img.size[0]
	height = img.size[1]
	pixels = img.load()
	
	y = 0
	while y < height:
		x = 8
		while x < width:
			pixels[x, y] = (0,0,0,0)
			x += 1
		y += 1
	
	img.save(file)