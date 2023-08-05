#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

labels = ['Farrah', 'Fred', 'Felicia']
width = 0.5

apples = fruit[0][:]
bananas = fruit[1][:]
orange = fruit[2][:]
peaches = fruit[3][:]

plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruits')

plt.bar(labels, apples, width, color='red')
plt.bar(labels, bananas, width, bottom=apples, color='yellow')
plt.bar(labels, orange, width, bottom=apples + bananas, color='#ff8000')
plt.bar(labels, peaches, width, bottom=apples + orange, color='#ffe5b4')

plt.legend(['apples', 'bananas', 'oranges', 'peaches'])
plt.yticks(np.arange(0, 90, step=10))
plt.show()
