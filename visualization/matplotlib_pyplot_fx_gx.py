import matplotlib.pyplot as plt 
import numpy as np 

# functions
def f(x):
    return np.exp(-x / 10) * np.sin(x * np.pi)

def g(x):
    return x * np.exp(-x / 3)

# interval
x = np.arange(0, 10, 0.1)
y_f = f(x)
y_g = g(x)

plt.plot(x, y_f)
plt.plot(x, y_g)

plt.title('f(x) & g(x)')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(['f(x)', 'g(x)'])

plt.savefig('plot.png', dpi=1000, bbox_inches='tight')
plt.show()
