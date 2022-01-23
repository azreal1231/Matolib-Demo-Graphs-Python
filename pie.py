import matplotlib.pyplot as plt


values = [40, 70]
names = ['test', 'test2']
plt.pie(values, labels=names, labeldistance=1.15, autopct='%1.1f%%')
plt.axis('equal')

plt.savefig('pie_test.png')