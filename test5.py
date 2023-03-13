import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import pandas as pd
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

df=pd.read_csv('subsurface_data.txt', delimiter=' ', names=['X','Y','Z'])
X=df.X
Y=df.Y
Z=df.Z
verts = [list(zip(X, Y, Z))]
# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create poly3d collection
poly = Poly3DCollection(verts, alpha=.25, facecolor='red')
ax.add_collection3d(poly)

# Set axis limits and labels
ax.set_xlim([min(X), max(X)])
ax.set_ylim([min(Y), max(Y)])
ax.set_zlim([min(Z), max(Z)])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
 

