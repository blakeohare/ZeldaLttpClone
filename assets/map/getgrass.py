import Image
img = Image.open('tiles\\library\\ground\\grass.png')
if img.mode != 'RGBA':
	img = img.convert('RGBA')

pixels = img.load()
print pixels[0, 0]