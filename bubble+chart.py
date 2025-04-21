import matplotlib.pyplot as plt
import numpy as np

x = [5, 7, 8, 7, 2, 17]
y = [99, 86, 87, 88, 100, 86]
size = [20, 100, 200, 150, 300, 250]

plt.scatter(x, y, s=size, alpha=0.5, color='purple')
plt.title('Bubble Chart')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
         