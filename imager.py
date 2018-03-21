import os
from PIL import Image

filename = raw_input('What is the filename?')
rootdir = 'C:/Users/joshu/Desktop/' + filename

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
		if not os.path.exists(os.path.join(rootdir,'images/', file[:-4] )):
			os.makedirs(os.path.join(rootdir,'images/',file[:-4] ))

		if file.endswith('.png'):
			print file
			im = Image.open(os.path.join(rootdir,file))

			for x in xrange(im.size[1]/48):
				#crop image
				i = im.crop((0, x * 48, im.size[0], x*48 + 48))
				i.save(os.path.join(rootdir,'images/',file[:-4], file[:-4] + '_' + str(x)) + '.png', "png")