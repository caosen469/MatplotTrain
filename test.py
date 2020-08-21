import matplotlib.pyplot as plt
import pandas
import numpy as np

# %%

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4], [4, 2, 1, 3])

plt.plot([1, 2, 3, 4], [4, 2, 1, 3])

fig = plt.figure()
fig, ax = plt.subplots()

fig, ax = plt.subplots(2, 2)

# Types of input to plotting functions
# the input is expected to be numpy.array or numpy.ma.masked_array
# Pandas and numpy.matrix do not work here
a = pandas.Da

# using Objected-Oriented style
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()  # create a figure and an axes
ax.plot(x, x, label='linear')
ax.plot(x, x ** 2, label='quadratic')
ax.plot(x, x ** 3, label='cubic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()  # add a legend

# pyplot style

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # plot the same data on the implicit axes
plt.plot(x, x ** 2, label='quadratic')
plt.plot(x, x ** 3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple Plot')
plt.legend()


# Build a function to draw the graph

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    -----------
    :param ax: Axes
            The axes to draw to
    :param data1: array
                The x array data
    :param data2: array
                The y arrary data
    :param param_dict: dict
                    Dictionary of kwargs to pass to ax.plot
    :return:
    -----
    out: list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


# using the function
data1, data2, data3, data4 = np.random.randn(100, 4)

fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
