import Image
import os
import random

class TileLibrary:
	
	def __init__(self):
		self.pixelsToIds = {}
		self.idsToPixels = {}
		self.max_id = 0
		self.initialize_primitives()
		self.initialize_composites()
		
	def initialize_primitives(self):
		lines = read_file_lines(os.path.join('tiles', 'library.txt'))
		
		for line in lines:
			parts = line.split('\t')
			id = trim(parts[0])
			image = os.path.join('tiles', 'library', parts[2].split(',')[0].replace('/', os.sep) + '.png')
			pixel_list = create_color_array(image)
			self.add_basic(pixel_list, id)
			if id > self.max_id: self.max_id = id
			
	def initialize_composites(self):
		
		lines = read_file_lines(os.path.join('tiles', 'composites.txt'))
		
		
		for line in lines:
			
			ids = line.split('\t')
			
			output = self.idsToPixels[ids[0]][:]
			i = 1
			while i < len(ids):
				image = self.idsToPixels[ids[i]]
				for x in xrange(256):
					if image[x][3] > 0:
						output[x] = image[x]
				i += 1
			self.add_composite(output, ids)

	def add_composite(self, pixel_list, id_list):
		value = (pixel_list, id_list[:])
		hash = self.generate_tile_hash(pixel_list)
		if self.pixelsToIds.has_key(hash):
			self.pixelsToIds[hash].append(value)
		else:
			self.pixelsToIds[hash] = [value]
			
	def add_unknown(self, pixel_list, temp_id):
		self.add_composite(pixel_list, [temp_id])
		self.idsToPixels[temp_id] = pixel_list
	
	def add_basic(self, pixel_list, id):
		self.add_composite(pixel_list, [id])
		self.idsToPixels[id] = pixel_list
	
	def get_tile(self, id):
		return self.idsToPixels.get(id)
	
	def get_ids(self, pixel_list):
		hash = self.generate_tile_hash(pixel_list)
		
		if self.pixelsToIds.has_key(hash):
			bucket = self.pixelsToIds[hash]
			for item in bucket:
				if self.are_pixels_same(pixel_list, item[0]):
					return item[1]
		return None
	
	def are_pixels_same(self, a, b):
		if a[54] != b[54]: return False
		for i in xrange(256):
			if a[i][0] != b[i][0]: return False
			if a[i][1] != b[i][1]: return False
			if a[i][2] != b[i][2]: return False
			if a[i][3] != b[i][3]: return False
		return True
	
	def generate_tile_hash(self, tile_pixel_list):
		return str(tile_pixel_list)
		a = tile_pixel_list[0]
		return str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + ' ' + str(a[3])
		
def open_image(imagepath):
	image = Image.open(imagepath)
	if image.mode != 'RGBA':
		image = image.convert('RGBA')
	return image

def create_color_array(imagepath):
	image = open_image(imagepath)
	pixels = image.load()
	output = []
	width = image.size[0]
	height = image.size[1]
	for y in xrange(0, height):
		for x in xrange(0, width):
			output.append(pixels[x, y])
	return output

def trim(string):
	ws = ' \n\r\t'
	while len(string) > 0 and string[0] in ws:
		string = string[1:]
	while len(string) > 0 and string[-1] in ws:
		string = string[:-1]
	return string

# remove comments denoted by # and blank lines
def read_file_lines(filename):
	c = open(filename, 'rt')
	lines = c.read().split('\n')
	c.close()
	output = []
	for line in lines:
		line = trim(line)
		if len(line) == 0: continue
		if line[0] == '#': continue
		output.append(line)
	return output

def get_unidentified_file_starting_number():
	# File names are in the format of "img123.png". Get the number of the last file
	# PNG files with different naming schemes should not appear in this folder ever
	files = filter(lambda x:x.endswith('.png'), os.listdir(os.path.join('tiles', 'unidentified')))
	if len(files) > 0:
		return int(files[-1][3:-4]) + 1
	return 1

def generate_unknown_tiles(imagepath):
	image = open_image(imagepath)
	map_pixels = image.load()
	width = (image.size[0] // 16) * 16
	height = (image.size[1] // 16) * 16
	library = get_library()
	
	temporary_manifest = []
	temp_id = 1
	tile = Image.new('RGBA', (16, 16))
	tile_pixels = tile.load()
	
	filenum = get_unidentified_file_starting_number()
	
	tile_pixel_list = [0] * 256
	
	map_width = width / 16
	map_height = height / 16
	layer = [0] * (map_width * map_height)
	j = 0
	for row in xrange(0, height / 16):
		print "Row:", row
		for col in xrange(0, width / 16):
			i = 0
			for py in xrange(0, 16):
				for px in xrange(0, 16):
					c = pixels[px + col * 16, py + row * 16]
					v = (c[0], c[1], c[2], 255)
					tile_pixels[px, py] = v
					tile_pixel_list[i] = v
					i += 1
			tile_ids = library.get_ids(tile_pixel_list)
			
			if tile_ids == None:
				tile.save(os.path.join('tiles', 'unidentified', 'img' + str(filenum) + '.png'))
				tile_id = 't' + str(temp_id)
				library.add_unknown(tile_pixel_list, tile_id)
				temp_line = "\t".join([tile_id, "t", "unidentified/img" + str(filenum)])
				temporary_manifest.append(temp_line)
				tile_ids = [tile_id]
				filenum += 1
				temp_id += 1
			elif len(tile_ids) == 0:
				print col, row
				return
			
			layer[j] = '|'.join(tile_ids)
			
			j += 1
			
	print "Writing temporary manifest..."
	write_temporary_manifest(temporary_manifest)
	
	serialize_input_map(map_width, map_height, ','.join(layer))

def serialize_input_map(width, height, layer_contents):
	print "Serializing input map to map file"
	
	output = []
	output.append('#width:' + str(width))
	output.append("#height:" + str(height))
	output.append("#layer1:" + layer_contents)
	
	
	c = open('map_file.txt', 'wt')
	c.write('\n'.join(output))
	c.close()

class ToBlitObject:
	def __init__(self, image):
		self.column = -1
		self.row = -1
		self.image = image
		self.pixels = image.load()
		self.temporary = False
	
	def Blit(self, target, x, y):
		left = x
		top = y
		y = 0
		pixels = self.pixels
		while y < 16:
			x = 0
			while x < 16:
				value = self.pixels[x, y]
				target[x + left, y + top] = value
				x += 1
			y += 1

def write_temporary_manifest(manifest):
	permanent_manifest = read_file_lines('tiles' + os.sep + 'library.txt')
	output = []
	
	"""
	format of manifest consumed by code is as follows:
	
	ID
	physics - comma delimited if subdefined
	column on grand image - 0 indexed
	row on grand image - 0 indexed
		row and column are comma-delimited
		each set of image coordinates is |-delimited
	codes
		these are commad delimited
	
	"""
	to_blit = []
	manifest_lines = []
	
	for lines in (permanent_manifest, manifest):
		is_unknown = lines == manifest
		for line in lines:
			parts = line.split('\t')
			id = parts[0]
			physics = parts[1]
			images = parts[2].split(',')
			if len(parts) == 4:
				codes = parts[3].split(',')
			else:
				codes = []
			new_line = [id, physics, [], codes]
			
			for image in images:
				if not image.startswith('unidentified'):
					image = 'library/' + image
				imagefile = 'tiles' + os.sep + image.replace('/', os.sep) + '.png'
				
				tbo = ToBlitObject(Image.open(imagefile))
				tbo.temporary = is_unknown
				to_blit.append(tbo)
				new_line[2].append(tbo)
			manifest_lines.append(new_line)
	print "final manifest has", len(manifest_lines), "lines"
	print len(to_blit), "images total"
	
	images_total = len(to_blit)
	width = int(images_total ** .5)
	height = int((images_total - 1) / width) + 1
	
	print "Rendering tile source image..."
	grand_image = Image.new('RGBA', (width * 16, height * 16))
	target_pixels = grand_image.load()
	slots = []
	for y in xrange(height):
		for x in xrange(width):
			slots.append((x, y))
	
	random.shuffle(slots)
	
	for tbo in to_blit:
		xy = slots[0]
		slots = slots[1:]
		x = xy[0]
		y = xy[1]
		tbo.column = x
		tbo.row = y
		tbo.Blit(target_pixels, x * 16, y * 16)
		if tbo.temporary:
			for i in xrange(16):
				target_pixels[x * 16 + i, y * 16] = (255, 0, 0, 255)
				target_pixels[x * 16, y * 16 + i] = (255, 0, 0, 255)
				target_pixels[x * 16 + i, y * 16 + 15] = (255, 0, 0, 255)
				target_pixels[x * 16 + 15, y * 16 + i] = (255, 0, 0, 255)
				
	
	grand_image.save('tiles.png')
	
	print "Writing out consumption-ready manifest..."
	
	output = []
	for line in manifest_lines:
		try:
			id = line[0]
			physics = line[1]
			images = line[2]
			newline = id + '\t' + physics + "\t"
			for i in xrange(len(images)):
				images[i] = str(images[i].column) + ',' + str(images[i].row)
			newline += "|".join(images)
			
			if len(line) == 4:
				newline += "\t" + ','.join(line[3])
			output.append(newline)
		except:
			print("This line is bad: " + str(line))
	
	c = open('tile_manifest.txt', 'wt')
	c.write("\n".join(output))
	c.close()
	
	print "Done!"
library = TileLibrary()

def get_library():
	global library
	return library
	
image = Image.open('light_world.png')
if image.mode != 'RGB':
	image = image.convert('RGB')
pixels = image.load()
width = image.size[0]
height = image.size[1]

generate_unknown_tiles('light_world.png')