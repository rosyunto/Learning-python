from die import Die
import pygal
import matplotlib.pyplot as plt

die = Die()
die1 = Die()

results = []
for roll_num in range(1000):
    result = die.roll() + die1.roll()
    results.append(result)
#print(results)

#统计每个点数出现的频率
frequencies = []
max_num_sides = die.num_sides + die1.num_sides
for value in range(2, max_num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)

#对结果进行可视化-柱状图
'''
hist = pygal.Bar()

hist._title = 'Result of rolling one D6 1000 times.'
hist.x_labels = list(range(2, max_num_sides+1))
hist._x_title = 'Result'
hist._y_title = 'Frequency of result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual2.svg')
'''
#对结果进行可视化-线图
plt.scatter(list(range(2, max_num_sides+1)), frequencies)
plt.xlabel('Points')
plt.ylabel('Times')
plt.show()