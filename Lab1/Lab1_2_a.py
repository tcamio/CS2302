'''
This program write a recursive method to draw given figures in CS2302 Lab1,
Question 2.
'''

import matplotlib.pyplot as plt
import numpy as np
import math 

# Create a list of x- and y- coordination based on center and rad
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

'''
draw_circles draws circles recursively. The first circle is drawn based on the
given center and radius. The consecutive squares are drawn with weighted radius
radius*w and the x-coordination of the center is shifted -radius*(1-w).
'''
def draw_circles(ax,n,center,radius,w):
    if n>0:
        # Create and draw a crcle based on given center and radius
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        # The center of next circle is shifted and call draw_circles
        center[0]=center[0]-radius*(1-w)
        draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Lab1_2_a.png')