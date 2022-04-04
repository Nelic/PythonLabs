import matplotlib.pyplot as plt
import numpy as np
import math

# plt.plot([1,3,2,4])
# plt.show()

# task1
# x = linspace(-2, 5, 100)
# y = x * sin(x * 5)
# plt.plot(x, y)
# plt.savefig('Task1.png', dpi=150)

# task2
# str = "English for texts for giving for English for"
# s = str.split(" ")
# x=range(len(s))
# print(x)
# a = np.array(s)
# plt.hist(a, bins = x)
# plt.show()
# plt.savefig('Task2.png', dpi=150)

# task3
str = "English for. texts for giving! for English for. asoidhjo?iasdio asdj? oaisdjoi?"
dots = str.count(".")
hail = str.count("!")
quesion = str.count("?")
s = dots * "." + hail * "!" + quesion * "?"
s = list(s)
x = len(s)
a = np.array(s)
plt.hist(a, bins = x)
plt.show()
# plt.savefig('Task2.png', dpi=150)