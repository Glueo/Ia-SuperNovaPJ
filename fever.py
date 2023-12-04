import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 计数零点为21月3号下午5点
times = np.array([0, 4, 7, 16, 19, 21, 22])

temp = np.array([38.5, 39.3, 38.0, 37.0, 36.0, 37.0, 37.1])

m = make_interp_spline(times, temp)
xs = np.linspace(times.min(), times.max(), 500)
ys = m(xs)
plt.plot(xs, ys)
plt.scatter(times, temp, color="blue")
plt.axhline(37, color="green", linestyle="--")
plt.axhline(39, color="red", linestyle="--")

plt.xlabel("Hours(start from Dec.3rd 17:00)/h")
plt.ylabel("Temperature/celsius")
plt.show()
