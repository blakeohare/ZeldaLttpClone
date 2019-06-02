import Image
import os
import random

class Sprite:
	def __init__(self, id, width, height, pixelList):
		self.id = id
		self.width = width
		self.height = height
		self.pixels = pixelList
		self.offsetX = 0
		self.offsetY = 0

def blit(source, target, left, top, sourceWidth, sourceHeight):
	y = 0
	while y < sourceHeight:
		x = 0
		while x < sourceWidth:
			v = source[x, y]
			#print x, left, y, top
			target[x + left, y + top] = v
			x += 1
		y += 1

def trim(string):
	whitespace = ' \n\r\t'
	while len(string) > 0 and string[0] in whitespace:
		string = string[1:]
	while len(string) > 0 and string[-1] in whitespace:
		string = string[:-1]
	return string

def get_sprites():
	c = open('image_directory.txt', 'rt')
	lines = c.read().split('\n')
	c.close()
	output = []
	for line in lines:
		line = trim(line)
		if len(line) > 0 and line[0] != '#':
			parts = line.split('\t')
			if len(parts) == 2 or len(parts) == 4:
				id = parts[0]
				image = Image.open('raw_images' + os.sep + parts[1])
				if image.mode != 'RGBA':
					image = image.convert('RGBA')
				
				sprite = Sprite(id, image.size[0], image.size[1], image.load())
				
				if len(parts) == 4:
					sprite.offsetX = int(parts[2])
					sprite.offsetY = int(parts[3])
				
				output.append(sprite)
			else:
				print("Unrecognized row: " + line)
	return output

sprites = get_sprites()
maxwidth = 0
maxheight = 0

for sprite in sprites:
	if sprite.width > maxwidth: maxwidth = sprite.width
	if sprite.height > maxheight: maxheight = sprite.height

numsprites = len(sprites)

maxwidth += 1
maxheight += 1

outputColumns = int(numsprites ** 0.5 + 1)
outputRows = int(numsprites / outputColumns + 1)

outputWidth = outputColumns * maxwidth
outputHeight = outputColumns * maxheight

random.shuffle(sprites)

canvas = Image.new('RGBA', (outputWidth, outputHeight))
canvasPixels = canvas.load()

manifest = []

col = 0
row = 0
while len(sprites) > 0:
	sprite = sprites[0]
	blit(sprite.pixels, canvasPixels, col * maxwidth, row * maxheight, sprite.width, sprite.height)
	
	line = sprite.id + '\t' + str(col * maxwidth) + ',' + str(row * maxheight)
	line += '\t' + str(sprite.width) + ',' + str(sprite.height)
	if sprite.offsetX != 0 or sprite.offsetY != 0:
		line += '\t' + str(sprite.offsetX) + ',' + str(sprite.offsetY)
	
	manifest.append(line)
	
	sprites = sprites[1:]
	
	col += 1
	if col >= outputColumns:
		col = 0
		row += 1

canvas.save('sprites.png')

c = open('sprite_manifest.txt', 'wt')
c.write('\r\n'.join(manifest))
c.close()