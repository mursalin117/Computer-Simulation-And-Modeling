import numpy as np
import random
import matplotlib.pyplot as plt

xb, yb = np.random.randint(0, 1000, 2)
xf, yf = np.random.randint(0, 1000, 2)
vf = 20
thresholdDist= 100
maxDist = 900

fx = []
fy = []
bx = []
by = []

fx.append(xf)
fy.append(yf)
bx.append(xb)
by.append(yb)

cnt = 0

while (True):
    cnt += 1
    dist = np.sqrt((xb-xf)**2+(yb-yf)**2)
    print(dist)
    if (dist >= maxDist):
        flag = False
        print('Bomber escaped at step' + str(cnt))
        break
    elif (dist <= thresholdDist):
        flag = True
        print('Bomber caught at step ' + str(cnt))
        break
    else:
        sinA, cosA = (yb-yf)/dist, (xb-xf)/dist
        xf, yf = (xf+vf*cosA), (yf+vf*sinA)
        xb, yb = np.random.randint(0, 1000, 2)
        fx.append(xf)
        fy.append(yf)
        bx.append(xb)
        by.append(yb)

plt.scatter(fx, fy)
plt.scatter(bx, by)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Bomber Vs Fighter\nBomber caugth =' + ('True' if flag == True else 'False') + ' at step ' + str(cnt))
plt.legend(['Fighter', 'Bomber'])
plt.show()
