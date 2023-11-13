from pylab import *

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
show()