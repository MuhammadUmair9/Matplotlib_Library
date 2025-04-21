import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
populations = [450, 460, 470, 480, 490, 510, 530, 550, 570, 590, 610]

plt.plot(years, populations, label="populations", marker='o', linestyle='--', color='green')
plt.title("Population growth of the City")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
