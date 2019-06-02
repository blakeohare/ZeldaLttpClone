import os

id = 110
file_num = 1

#Physics
# g - ground
# s - short blocking
# t - tall blocking
# h - hole
# f - foliage
# w - shallow water
# d - deep water
# i - ice
# j - jump down
# nw - diagonal northwest
# ne - diagonal northeast
# sw - diagonal southwest
# se - diagonal southeast

physics = 't'

manifest = []

folder = 'blockingwall'

for file in os.listdir('.'):
	if file.endswith('.png'):
		filename = str(file_num) + '.png'
		os.rename(file, filename)
		
		line = str(id) + '\t' + physics + '\t' + folder + os.sep + filename[:-4]
		
		manifest.append(line)
		
		id += 1
		file_num += 1
	
text = '\n'.join(manifest)

c = open('manifest additions.txt', 'wt')
c.write(text)
c.close()