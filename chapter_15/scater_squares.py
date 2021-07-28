import matplotlib.pyplot as plt

#x_value = [1, 2, 3, 4, 5]
#y_value = [1, 4, 9, 16, 25]
x_value = list(range(1, 100))
y_value = [x**2 for x in x_value]
#plt.scatter(x_value, y_value, c = 'red', edgecolor = 'none', s = 40)
plt.scatter(x_value, y_value, c = y_value, cmap = plt.cm.Blues, edgecolor = 'none', s = 40)

plt.title('Square numbers', fontsize = 24)
plt.xlabel('values', fontsize = 14)
plt.ylabel('squares of value', fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 14)
plt.axis([0, 101, 0, 11000])

#plt.show()
plt.savefig('squares_plot.png', bbox_inches= 'tight')