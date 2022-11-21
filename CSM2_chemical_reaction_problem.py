import numpy as np

def main():
    a = [100]
    b = [50]
    c = [0]
    dt = 0.1
    t = [0]
    k1 = 0.008
    k2 = 0.002
    N = 60

    for i in range(N):
        temp_a = a[-1]
        temp_b = b[-1]
        temp_c = c[-1]
        temp_t = t[-1]
        
        a.append(temp_a + (k2*temp_c - k1*temp_a*temp_b)*dt)
        b.append(temp_b + (k2*temp_c - k1*temp_a*temp_b)*dt)
        c.append(temp_c + (2*k1*temp_a*temp_b - 2*k2*temp_c)*dt)
        t.append(temp_t + dt)
    
    print('Time', '\t', 'A(i)', '\t', 'B(i)', '\t', 'C(i)')
    for i in range(N+1):
        # print('%.2f' %t[i], '\t%.2f' %a[i], '\t%.2f' %b[i], '\t%.2f' %c[i])
        print(np.round(t[i], 2), '\t', np.round(a[i], 2), '\t', np.round(b[i], 2), '\t', np.round(c[i], 2))

    
if __name__ == '__main__':
    main()