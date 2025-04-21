import matplotlib.pyplot as plt

departments = ['CS', 'IT', 'SE', 'AI', 'DS']
number_of_students = [120, 100, 90, 60, 80]
color = ['green', 'yellow', 'blue', 'red', 'purple']

plt.bar(departments, number_of_students, color=color)
plt.title("Bar chart for number of students in different departments")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()