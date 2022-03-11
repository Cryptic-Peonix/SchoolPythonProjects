import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
plt.subplot(311) #num rows, num columns, fig number
plt.plot(t, t, 'r--')
plt.title("linear")
plt.subplot(312)
plt.plot(t, t**2, 'bs')
plt.plot(t, t**3,'g^')
plt.title("quadratic and cubic")
plt.ylabel("subplot 2 y axis")
plt.subplot(313)
plt.plot(t, np.cos(t),'k')
plt.axis([0,np.pi,-1.5, 1.5])
plt.grid(True)
plt.show()





