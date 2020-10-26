import matplotlib.pyplot as plt
import numpy as np
'''
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1,sharex=True)#sharex=True

ax1.fill_between(x, 0, y1,)
ax1.set_tit('between y1 and 0')

ax2.fill_between(x, y1, 1)
ax2.set_xlabel('between y1 and 1')

ax3.fill_between(x, y1, y2)
ax3.set_xlabel('between y1 and y2')
ax3.set_xlabel('x')
plt.show()
'''
#fig = plt.figure()  # an empty figure with no axes
#fig.suptitle('No axes on this figure')  # Add a title so we know which it is
#fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

'''x = np.linspace(1, 10, 1000)
plt.plot(x, x, label='sample1', color='b')
plt.plot(x, x**2, label='sample2', color='r')
plt.plot(x, x**3, label='sample3', color='g')
plt.suptitle("just kidding")
plt.legend()
plt.show()'''
#simple graph in plt
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:

'''
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'o'})
plt.show()
'''
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
d = np.linspace(0, 50, 50)
plt.subplot(131)
plt.scatter('a', 'b', c='d', s='d', data=data)
plt.subplot(132)
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
np.random.randint()