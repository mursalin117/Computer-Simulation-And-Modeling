import numpy as np
import matplotlib.pyplot as plt

def main():
    xb, yb = np.random.randint(-500, 500, 2)
    xf, yf = np.random.randint(-500, 500, 2)
    vf = 20
    minDist = 100
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

    while(True):
        cnt += 1
        dist = np.sqrt((xb-xf)**2+(yb-yf)**2)
        print(dist)
        if (dist <= minDist):
            flag = True
            print('Bomber caught at step: ' + str(cnt))
            break
        elif (dist >= maxDist):
            flag = False
            print('Bomber escaped at step: ' + str(cnt))
            break
        else:
            cosA, sinA = (xb-xf)/dist, (yb-yf)/dist
            xf, yf = (xf+vf*cosA), (yf+vf*sinA)
            xb, yb = np.random.randint(-500, 500, 2)
            fx.append(xf)
            fy.append(yf)
            bx.append(xb)
            by.append(yb)

    plt.scatter(fx, fy)
    plt.scatter(bx, by)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Bomber vs Fighter\nBomber ' + ('caught' if flag == True else 'escaped') + ' at step: ' + str(cnt)) 
    plt.legend(['Fighter', 'Bomber'])
    plt.savefig('Pure-Persuit.jpeg')
    plt.show()

if __name__ == '__main__':
    main()