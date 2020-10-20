import matplotlib.pyplot as plt
import numpy as np

plt.plot([10, 20, 30, 40], [0.0004019737243652344,  0.02113485336303711, 2.5640463829040527, 324.08351135253906], marker= "x")
plt.xlabel("n")
plt.ylabel("time, t(s)")
plt.show()

time_series = [2.5640463829040527, 324.08351135253906]
n = [20, 40]
slope, intercept = np.polyfit(np.log(n), np.log(time_series), 1)
print(slope)