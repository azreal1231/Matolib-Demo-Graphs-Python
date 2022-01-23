import matplotlib.pyplot as plt

data = [23, 45, 56, 78, 213]
plt.bar([1, 2, 3, 4, 5], data)
# plt.show()
plt.savefig('bar_test.png')