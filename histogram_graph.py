import matplotlib.pyplot as plt

categories = [12, 13, 17, 18, 15, 18, 18, 19, 22, 22, 17, 21, 20, 23, 25, 26, 28]


n, bins, patches = plt.hist(categories, bins=5, edgecolor='black')
colors = x = ['red', 'green', 'black', 'yellow', 'purple']
for patch, color in zip(patches, colors):
    patch.set_facecolor(color)
plt.title('Histogram Example')
plt.xlabel('values')
plt.ylabel('frequency')

plt.show()
