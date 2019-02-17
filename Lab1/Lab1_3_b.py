'''
This program writes a recursive method to draw given figures in CS2302 Lab1,
Question 3.
'''
import matplotlib.pyplot as plt

'''
Create a list of x- and y- coordination based on number of iteration,
the coordination of parent point, and depth and width, which define the size of
canvas.
'''
def binary_tree(n, parent, depth, width):
    x = [parent[0]-width/4, parent[0], parent[0]+width/4]
    y = [parent[1]-depth/n, parent[1], parent[1]-depth/n]
    return x, y

'''
draw_tree draws binary tree recursively. r represents the remaining number of
iteration and n represents the number of iteration in total. parent, depth,
and width are as same as binary_tree, the coordination of parent point and the
size of drawing canvas.
'''
def draw_tree(ax, r, n, parent, depth, width):
    if r>0:
        # Create and draw a binary tree based on given variables.
        x, y = binary_tree(n, parent, depth, width)
        ax.plot(x, y, color='K')
        
        # Repeat to left and right of the binary tree.
        draw_tree(ax, r-1, n, [parent[0]-width/4, parent[1]-depth/n], depth, width/2)
        draw_tree(ax, r-1, n, [parent[0]+width/4, parent[1]-depth/n], depth, width/2)

plt.close("all") 
fig, ax = plt.subplots()
remIterate = 4
numIterate = remIterate
parentCoordinate = [0, 0]
depth = 500
width = 500
draw_tree(ax, remIterate, numIterate, parentCoordinate, depth, width)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('Lab1_3_b.png')
