from pylab import *
import numpy as np

'''
def initialize(x0,y0):
    global x,y,xres,yres
    x = x0
    y = y0
    xres = [x]
    yres = [y]

def observe():
    global x, y, xres,yres
    xres.append(x)
    yres.append(y)

def update():
    global x, y, xres,yres
    nextx = .5 * x + y
    nexty = -.5 *x + y
    x,y = nextx,nexty

for x0 in arange(-2,2,.5):
    for y0 in arange(-2,2,.5):
        initialize(x0,y0)
        for t in range(30):
            update()
            observe()
        print(len(xres))
        print(len(yres))
        print("\n***********************\n", xres)
        print("\n***********************\n", yres)
        plot(xres,yres)
'''

t_image = np.array([[[ 0.67826139,  0.29380381],
                     [ 0.90714982,  0.52835647],
                     [ 0.4215251 ,  0.45017551]],

                   [[ 0.92814219,  0.96677647],
                    [ 0.85304703,  0.52351845],
                    [ 0.19981397,  0.27417313]],

                   [[ 0.60659855,  0.00533165],
                    [ 0.10820313,  0.49978937],
                    [ 0.34144279,  0.94630077]]])

def image2vector(image):
    dim = image.shape[0]*image.shape[1]*image.shape[2]
    print(dim)
    v = np.reshape(image,(dim,1))
    #v = np.reshape(-1,1)
    return v

print ("image2vector(image) = " + str(image2vector(t_image)))

print(np.zeros((3,1)))


x = np.random.rand(4,3)
y = np.sum(x,axis=1, keepdims=True)

print(y.shape)