#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# main title
plt.suptitle('All in One')

# 0-line.py
plt.subplot(3, 2, 1)
plt.xticks([0, 2, 4, 6, 8, 10])
plt.xlim([0, 10])
plt.yticks([0, 500, 1000])
plt.ylim([0, 1000])
plt.plot(y0, "r-")

# 1-scatter.py
plt.title('Men\'s Height vs Weigth')
plt.subplot(3, 2, 2)
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.scatter(x1, y1, color="magenta")

# 2-charge_scale.py
plt.title('Exponential Devay of C-14')
plt.subplot(3, 2, 3)
plt.ylabel('Fraction Remaining')
plt.xlabel('Time (years)')
plt.yscale('log')
plt.xlim(0, 28650)
plt.plot(x2, y2)

# 3-two.py
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.plot(x3, y31, '--', color='r')
plt.plot(x3, y32, color='g')
plt.legend(["C-14", "Ra-226"])
plt.show()

# 4-frequency.py
plt.title('Project A')
plt.ylabel('Number of Students')
plt.xlabel('Grades')
plt.ylim(0, 30)
plt.xlim(0, 100)
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.hist(student_grades, edgecolor='black', bins=[40, 50, 60, 70, 80, 90, 100])
plt.show()

plt.tight_layout()
plt.show()
