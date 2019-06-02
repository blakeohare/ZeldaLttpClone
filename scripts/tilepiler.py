import pygame
import sys

def main(args):
	
	pygame.init()
	scr = pygame.display.set_mode((400, 300))
	atlas = pygame.image.load('tiles.png').convert_alpha()
	
	c = open('tiles.txt', 'rt')
	t = c.read()
	c.close()
	lines = t.split('\n')
	counter = 0
	for line in lines:
		print(counter)
		counter += 1
		parts = line.split('\t')
		if len(parts) >= 3:
			s = pygame.Surface((16, 16), pygame.SRCALPHA)
			id = parts[0]
			flags = parts[1]
			images = parts[2].split('|')
			useSuffix = len(images) > 1
			suffix = 1
			for image in images:
				coords = image.split(',')
				col, row = coords
				x = int(col) * 16
				y = int(row) * 16
				metadata = parts[3] if len(parts) == 4 else None
				if metadata == 'canopy':
					pass #print(id)
				
				s.blit(atlas, (-x, -y))
				filename = 'TilePile\\' + id
				if useSuffix:
					filename += '_anim' + str(suffix)
					suffix += 1
				filename += '.png'
				pygame.image.save(s, filename)

main(sys.argv[1:])
