'''subplots'''

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [5, 10, 15, 20, 25]

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# # ax1.plot(x,y)
# ax1.scatter(x,y)
# plt.show()

'''data visualization'''


# import matplotlib.pyplot as plt
# xaxis = [1, 2, 3, 4, 5]
# yaxis = [7, 50, 24, 44, 54]

# # plt.scatter(xaxis,yaxis)
# plt.plot(xaxis,yaxis)
# plt.xlabel('Number of incidents')
# plt.ylabel('occurance')
# plt.show()

'''live trend animation'''

import  matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')


def animate(i):
    data = open('csv.csv', 'r').read()
    lines = data.split('\n')
    xs = []
    ys = []

    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.plot(xs, ys)


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
