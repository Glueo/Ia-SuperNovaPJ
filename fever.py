import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 计数零点为21月3号下午5点

times = np.array([-5,0, 4, 7, 16, 19, 21, 22,23,26,26.5 ,27.25,27.45,28.5,29,29.5,30.25,
                  40.5,44,47,47.9,52.25,54,55,59,60,
                  64.25,66.5,68.5,70,71,74,75,76.5,78,
                  90.75,95.75])

temp = np.array([38,38.5, 39.3, 38.0, 37.0, 36.0, 37.0, 37.1,37.3,39.2,38.9,38.6,39.4,38.5,37.75,37.5,37.0,
                 35.8,36.1,36.7,36.5,36.6,37.5,37.4,37.4,37.3,
                 37.8,37.3,37.3,37.4,37.5,38,38.2,38.2,38,
                 36.4,36.5])

plt.plot(times,temp )
plt.scatter(times, temp, color="blue")

#吃药了
plt.scatter([4,27.45],[39.3,39.4],color='red')


plt.axvline(7,color = 'yellow',linestyle = '-.')
plt.axvline(7+24,color = 'yellow',linestyle = '-.')
plt.axvline(7+24+24,color = 'yellow',linestyle = '-.')
plt.axvline(7+24+24+24,color = 'yellow',linestyle = '-.')

plt.axhline(37.3, color="green", linestyle="--")
plt.axhline(38, color="blue", linestyle="--")
plt.axhline(39, color="red", linestyle="--")
#plt.axhline(41, color="black", linestyle="--")

plt.xlabel("Hours(start from Dec.3rd 17:00)/h")
plt.ylabel("Temperature/celsius")
plt.show()
