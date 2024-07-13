import imageio.v3 as iio

#stores location of image files
filenames = ['egg1.jpg', 'egg2.jpg', 'egg3.jpg']

#stores actual image data 
images = []

#iterates through each file path and loads that image 
for filename in filenames:
    images.append(iio.imread(filename))

#converts loaded images into GIF 
iio.imwrite('egg.gif', images, duration=500, loop=0)




