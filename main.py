import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 20, 18]

plt.plot(x, y, marker='o')
plt.title("نمودار خطی")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()



students = ["علی", "رضا", "مریم", "سارا"]
scores = [18, 19, 17, 20]


plt.bar(students, scores, color="skyblue")
plt.title("نمرات دانش‌آموزان")
plt.ylabel("نمره")
plt.show()


students = ["علی", "رضا", "مریم", "سارا"]
scores = [18, 19, 17, 20]

plt.bar(students, scores, color="skyblue")
plt.title("نمرات دانش‌آموزان")
plt.ylabel("نمره")
plt.show()


import numpy as np

data = np.random.randint(10, 20, size=50)  # ۵۰ نمره تصادفی
plt.hist(data, bins=5, color="orange", edgecolor="black")
plt.title("توزیع نمرات")
plt.xlabel("بازه نمرات")
plt.ylabel("تعداد")
plt.show()
