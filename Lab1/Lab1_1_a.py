'''
This program write a recursive method to draw given figures in CS2302 Lab1,
Question 1.
'''

import matplotlib.pyplot as plt
import time

# Create a list of x- and y- coordination based on center and side
def square(center, side):
    x = [center[0]-1*side/2, center[0]-1*side/2, center[0]+side/2, center[0]+side/2, center[0]-1*side/2]
    y = [center[1]-1*side/2, center[1]+side/2, center[1]+side/2, center[1]-1*side/2, center[1]-1*side/2]
    return x, y

'''
draw_squares draws squares recursively. The first square is drawn based on the
given center and side. The consecutive squares are drawn from bottom left, 
top left, top right, and bottom right cornor respectively. The user can specify
how the consecutive squares change their side by variable w.
'''
def draw_squares(ax,n,center,side,w):
    if n>0:
        # Create and draw a square based on given center and side.
        x, y = square(center, side)        
        ax.plot(x, y, color='K')
              
        # Repeat to each corner of the square
        draw_squares(ax, n-1, [center[0]-side/2, center[1]-side/2], side*w, w)
        draw_squares(ax, n-1, [center[0]-side/2, center[1]+side/2], side*w, w)
        draw_squares(ax, n-1, [center[0]+side/2, center[1]+side/2], side*w, w)
        draw_squares(ax, n-1, [center[0]+side/2, center[1]-side/2], side*w, w)

plt.close("all")
center = [0, 0] 
side = 800
weight = 0.5
numRepeat = 2
fig, ax = plt.subplots()

# start mesureing time
start = time.time()

draw_squares(ax, numRepeat, center, side, weight)

# print time elapsed
elapsed_time = time.time() - start
print("elapsed_time:{:.6g}".format(elapsed_time) + "[sec]")

ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Lab1_1_a.png')