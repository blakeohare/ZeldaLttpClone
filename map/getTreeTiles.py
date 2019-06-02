import os
import Image

def blit(source, target, sourceX, sourceY, width, height, targetX, targetY):
	y = 0
	while y < height:
		x = 0
		while x < width:
			target[targetX + x, targetY + y] = source[sourceX + x, sourceY + y]
			x += 1
		y += 1

def convertToTiles(pixels, width, height, starting_i):
	tile = Image.new('RGBA', (16, 16))
	target = tile.load()
	i = starting_i
	for row in range(height // 16):
		for col in range(width // 16):
			top = row * 16
			left = col * 16
			y = 0
			while y < 16:
				x = 0
				while x < 16:
					target[x, y] = pixels[left + x, top + y]
					x += 1
				y += 1
			tile.save('Tree' + os.sep + 'leaves' + str(i) + '.png')
			tile.save('Tree' + os.sep + 'trunk' + str(i) + '.png')
			i += 1
	

image = Image.open('light_world.png')
if image.mode != 'RGBA':
	image = image.convert('RGBA')

left = 16 * 30
top = 16 * 32
right = left + 4 * 16
bottom = top + 5 * 16
width = 64
height = 80
tree = Image.new('RGBA', (width, height))

lwpixels = image.load()
treepixels = tree.load()
bg = lwpixels[left, top]
y = 0
while y < height:
	x = 0
	while x < width:
		v = lwpixels[x + left, y + top]
		if v != bg:
			treepixels[x, y] = v
		x += 1
	y += 1


treeoffset = Image.new('RGBA', (width + 16, height))
topixels = treeoffset.load()

blit(treepixels, topixels, 0, 0, width, height, 8, 0)

convertToTiles(treepixels, width, height, 1)
convertToTiles(topixels, width + 16, height, 21)

