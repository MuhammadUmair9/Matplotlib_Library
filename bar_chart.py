import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 2, 5]
x = ['green', 'yellow', 'blue', 'red']

plt.bar(categories, values, color=x)
plt.title('Bar chart')
plt.xlabel('Categories')
plt.ylabel('values')
plt.grid(True)
plt.show()
