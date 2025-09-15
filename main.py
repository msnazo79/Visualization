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
