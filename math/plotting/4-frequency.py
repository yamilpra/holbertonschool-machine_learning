#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.title('Project A')
plt.ylabel('Number of Students')
plt.xlabel('Grades')
plt.ylim(0, 30)
plt.xlim(0, 100)
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.hist(student_grades, edgecolor='black', bins=[40, 50, 60, 70, 80, 90, 100])
plt.show()
