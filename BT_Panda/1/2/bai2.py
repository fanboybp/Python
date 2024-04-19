import matplotlib.pyplot as plt
import numpy as np
x1 = (10, 20, 30)
y1 = (20, 40, 10)
plt.plot(x1, y1, label='line 1')
# plt.plot(x2, y2, label='line 2')

plt.legend(loc='upper left')
plt.axis([10,30,10,40])
plt.xticks(np.arange(10,30, 5))

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample graph!')
plt.show()
