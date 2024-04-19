import matplotlib.pyplot as plt
import numpy as np
x = (1, 2, 3)
y = (2, 4, 1)
plt.plot(x, y)
plt.axis([1,3,1,4])
plt.xticks(np.arange(1,3.1,0.5))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample graph!')
plt.show()
