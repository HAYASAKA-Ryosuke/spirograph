import numpy as np
import matplotlib.pyplot as plt

rc = 82  # 定円の半径
rm = 50  # 動円の半径
rd = 20  # 描画点の半径
theta = np.linspace(0, 50 * 2 * np.pi, 1000)

x = (rc - rm) * np.cos(theta) + rd * np.cos(((rc - rm) / rm) * theta)
y = (rc - rm) * np.sin(theta) - rd * np.sin(((rc - rm) / rm) * theta)

plt.plot(x, y)
plt.show()
