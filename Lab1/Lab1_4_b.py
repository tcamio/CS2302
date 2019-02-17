'''
This program writes a recursive method to draw given figures in CS2302 Lab1,
Question 4.
'''
import matplotlib.pyplot as plt
import numpy as np
import math 

# Create a list of x- and y- coordination based on center and side
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

'''
draw_circles draws circles recursively. The circle is drawn based on given
center and radius. Additional five circles are drawn inside the first cirle
in order of center, left, right, bottom, and top respectively.
'''
def draw_circles(ax,n,center,radius):
    if n>0:
        # Create and draw a circle based on given center and siradius.
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        # Repeat to each inside position of the circle
        draw_circles(ax, n-1, [center[0], center[1]], radius/3)
        draw_circles(ax, n-1, [center[0]-radius*2/3, center[1]], radius/3)
        draw_circles(ax, n-1, [center[0]+radius*2/3, center[1]], radius/3)
        draw_circles(ax, n-1, [center[0], center[1]-radius*2/3], radius/3)
        draw_circles(ax, n-1, [center[0], center[1]+radius*2/3], radius/3)


plt.close("all") 
fig, ax = plt.subplots() 
numIterate = 4
center = [0, 0]
radius = 100
draw_circles(ax, numIterate, center, radius)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Lab1_4_b.png')
