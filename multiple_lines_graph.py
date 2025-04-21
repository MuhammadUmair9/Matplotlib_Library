import matplotlib.pyplot as p

years = [2018, 2019, 2020, 2021, 2022]

product_A = [120, 135, 150, 160, 180]
product_B = [80, 100, 90, 110, 130]
product_C = [60, 65, 70, 85, 95]
product_D = [100, 120, 115, 140, 150]
product_E = [90, 85, 100, 120, 125]

p.plot(years, product_A, label="Product A", marker='o', linestyle='-', color='blue')
p.plot(years, product_B, label="Product B", marker='s', linestyle='--', color='green')
p.plot(years, product_C, label="Product C", marker='^', linestyle='-.', color='red')
p.plot(years, product_D, label="Product D", marker='x', linestyle=':', color='orange')
p.plot(years, product_E, label="Product E", marker='d', linestyle='-', color='purple')

p.xlabel("Years")
p.ylabel("Sales")
p.title("Sales Trends of 5 Products (2-18-2022)")
p.grid(False)
p.legend
p.show()

