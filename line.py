import matplotlib.pyplot as plt

# data to be plotted
x = ['2021-12-04', '2021-12-05', '2021-12-06']
y = [100, 10, 300]

# plotting
plt.title("Line graph")
plt.plot(x, y, color="orangered")

plt.savefig('line_test.png')