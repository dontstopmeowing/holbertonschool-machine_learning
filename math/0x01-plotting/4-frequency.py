#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
plt.xlim(0, 100)
plt.ylim(0, 30)
xLimit = np.arange(0, 110, 10)
yLimit = np.arange(0, 35, 5)
plt.xticks(xLimit)
plt.yticks(yLimit)
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.hist(student_grades, bins=xLimit, edgecolor='black', linewidth=1.2)
plt.show()
