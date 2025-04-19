import matplotlib.pyplot as plt

lenght = 1
dt = 0.1
k = 0.1
m = 1

def Deriv(y, v):
    dy = y - lenght
    a = -k*dy/m

    return v, a

def Euler_step(y,v,ky,kv,dt):
    y = y + ky * dt
    v = v + kv * dt

    return y,v

y = lenght + 0.3
v = 0

tt = []
yy = []



for i in range(10000):
    tt.append(i*dt)
    yy.append(y)

    k1y, k1v = Deriv(y, v)
    y_2, v_2 = Euler_step(y, v, k1y, k1v, dt/2)
    k2y, k2v = Deriv(y_2, v_2)
    y, v = Euler_step(y, v, k2y, k2v, dt)

plt.figure(figsize=(12,3))
plt.plot(tt,yy)
plt.show()
