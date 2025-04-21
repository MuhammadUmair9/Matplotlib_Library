import matplotlib.pyplot as plt

subjects = ["Math", "English", "Science", "History", "Computer"]

student_A = [85, 78, 90, 70, 95]
student_B = [88, 82, 85, 75, 80]
student_C = [75, 80, 78, 72, 85]


plt.plot(subjects, student_A, label="Student A", marker='o', linestyle='-', color='blue')
plt.plot(subjects, student_B, label="Student B", marker='s', linestyle='--', color='yellow')
plt.plot(subjects, student_C, label="Student C", marker='^', linestyle=':', color='red')

plt.title("Students marks compersion")
plt.xlabel("subjects")
plt.ylabel("students_marks")
plt.grid(True)
plt.legend()
plt.show()