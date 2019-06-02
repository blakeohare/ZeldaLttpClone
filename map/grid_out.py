import Image

image = Image.open('light_world.png')
if image.mode != 'RGB':
	image = image.convert('RGB')

pixels = image.load()

width = image.size[0]
height = image.size[1]

for y in xrange(0, height, 16):
	for x in xrange(0, width, 16):
		for px in xrange(0, 16):
			pixels[x + px, y] = (0,0,0)
		for py in xrange(1, 16):
			pixels[x, y + py] = (0,0,0)

image.save('lw_grid.png')

